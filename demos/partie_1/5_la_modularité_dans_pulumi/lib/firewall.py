import pulumi
import pulumi_gcp as gcp

def create_firewall(network_self_link, instance_tag, service_port):
    return gcp.compute.Firewall(
        "demo1firewall",
        gcp.compute.FirewallArgs(
            network=network_self_link,
            allows=[
                gcp.compute.FirewallAllowArgs(
                    protocol="tcp",
                    ports=[
                        "22",
                        service_port,
                    ],
                ),
            ],
            direction="INGRESS",
            source_ranges=[
                "0.0.0.0/0",
            ],
            target_tags=[
                instance_tag,
            ],
        ),
    )
