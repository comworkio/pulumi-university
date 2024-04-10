import pulumi
import pulumi_gcp as gcp

def create_network():
    return gcp.compute.Network(
        "demo1network",
        gcp.compute.NetworkArgs(
            auto_create_subnetworks=False,
        ),
    )

def create_subnet(network_id):
    return gcp.compute.Subnetwork(
        "demo1subnet",
        gcp.compute.SubnetworkArgs(
            ip_cidr_range="10.0.1.0/24",
            network=network_id,
        ),
    )
