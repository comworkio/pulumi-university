import pulumi
import pulumi_gcp as gcp

def create_instance(network_id, subnet_id, machine_type, os_image, metadata_startup_script, instance_tag, service_port, firewall_dependency):
    return gcp.compute.Instance(
        "demo1bis",
        gcp.compute.InstanceArgs(
            name="demo1bis",
            machine_type=machine_type,
            boot_disk=gcp.compute.InstanceBootDiskArgs(
                initialize_params=gcp.compute.InstanceBootDiskInitializeParamsArgs(
                    image=os_image,
                ),
            ),
            network_interfaces=[
                gcp.compute.InstanceNetworkInterfaceArgs(
                    network=network_id,
                    subnetwork=subnet_id,
                    access_configs=[
                        {},
                    ],
                ),
            ],
            service_account=gcp.compute.InstanceServiceAccountArgs(
                scopes=[
                    "https://www.googleapis.com/auth/cloud-platform",
                ],
            ),
            allow_stopping_for_update=True,
            metadata_startup_script=metadata_startup_script,
            tags=[
                instance_tag,
            ],
        ),
        pulumi.ResourceOptions(depends_on=[firewall_dependency]),
    )
