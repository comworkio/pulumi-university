import pulumi
import pulumi_gcp as gcp
from lib.network import create_network, create_subnet
from lib.firewall import create_firewall
from lib.instance import create_instance

# Import the program's configuration settings.
config = pulumi.Config()
machine_type = config.get("machineType", "f1-micro")
os_image = config.get("osImage", "debian-11")
instance_tag = config.get("instanceTag", "webserver")
service_port = config.get("servicePort", "80")

# Create network and subnet
network = create_network()
subnet = create_subnet(network.id)

# Create firewall
firewall = create_firewall(network.self_link, instance_tag, service_port)

# Define metadata startup script
metadata_startup_script = f"""#!/bin/bash
    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Hello, DevoxxFR!</title>
    </head>
    <body>
        <h1>Hello, DevoxxFR! 👋</h1>
        <p>Deployed with 💜 by <a href="https://pulumi.com/">Pulumi</a>.</p>
    </body>
    </html>' > index.html
    sudo python3 -m http.server {service_port} &
    """

# Create instance
instance = create_instance(network.id, subnet.id, machine_type, os_image, metadata_startup_script, instance_tag, service_port, firewall)

# Export instance details
instance_ip = instance.network_interfaces.apply(lambda interfaces: interfaces[0].access_configs[0].nat_ip)
pulumi.export("name", instance.name)
pulumi.export("ip", instance_ip)
pulumi.export("url", instance_ip.apply(lambda ip: f"http://{ip}:{service_port}"))
