import os
import pulumi

from pulumi import automation as auto
from pulumi_gcp import compute
import pulumi_gcp as gcp

from adapters.provider.ProviderAdapter import ProviderAdapter
from utils.common import unbase64
from utils.logger import log_msg
from utils.size import Size

_gcp_project_id = os.getenv('GCP_PROJECT_ID')
_google_app_cred_str = unbase64(os.getenv('GCP_APPLICATION_CREDENTIALS'))
_ami_image = os.getenv('GCP_AMI_IMAGE')

class GcpAdapter(ProviderAdapter):
    def size_to_type(self, size):
        if size == Size.S:
            return "e2-small"
        else:
            return "e2-medium"

    def create_instance(self, name, project, region, zone, size):
        vmtype = self.size_to_type(size)
        log_msg("INFO", "[GcpAdapter][create_instance] name = {}, project = {}, region = {}, zone = {}, vmtype = {}".format(name, project, region, zone, vmtype))
        def create_pulumi_program():
            ip_address = gcp.compute.Address(
                "external-ip",
                address_type = "EXTERNAL",
                region = region
            )

            firewall_tags = ["allow-ssh", "allow-http", "allow-https"]
            gcp_network = os.getenv('GCP_NETWORK')

            compute_firewall = compute.Firewall(
                "pulumi-university-firewall",
                project = _gcp_project_id,
                network = gcp_network,
                source_tags = firewall_tags,
                allows = [compute.FirewallAllowArgs(protocol = "tcp", ports = ["22", "80", "443"])]
            )

            compute_instance = compute.Instance(
                resource_name = name,
                name = name,
                tags = firewall_tags,
                project = _gcp_project_id,
                machine_type = self.size_to_type(size),
                zone = f'{region}-{zone}',
                boot_disk = compute.InstanceBootDiskArgs(
                    initialize_params = compute.InstanceBootDiskInitializeParamsArgs(
                        type = 'pd-standard',
                        size = 50,
                        image = _ami_image,
                    ),
                ),
                network_interfaces = [{
                    "network": compute_firewall.network,
                    "accessConfigs": [{
                        "nat_ip": ip_address.address,
                    }],
                }],
                service_account = compute.InstanceServiceAccountArgs(
                    scopes = ["https://www.googleapis.com/auth/cloud-platform"],
                )
            )

            pulumi.export("public_ip", compute_instance.network_interfaces[0].access_configs[0].nat_ip)

        stack = auto.create_or_select_stack(stack_name = name,
                                            project_name = project,
                                            program = create_pulumi_program)

        stack.set_config("gcp:project", auto.ConfigValue(_gcp_project_id))
        stack.set_config("gcp:credentials", auto.ConfigValue(_google_app_cred_str))
        stack.set_config("gcp:region", auto.ConfigValue(region))

        up_res = stack.up()

        return {
            'status': 'ok',
            'ip': up_res.outputs.get("public_ip").value
        }
