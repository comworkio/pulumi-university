provider "google" {
  project = "<YOUR_PROJECT_ID>"
  region  = "us-central1" # Set your desired region
}

variable "machine_type" {
  description = "Type de machine virtuelle"
  default     = "f1-micro"
}

variable "os_image" {
  description = "Image du système d'exploitation de la machine virtuelle"
  default     = "debian-11"
}

variable "instance_tag" {
  description = "Tag de l'instance"
  default     = "webserver"
}

variable "service_port" {
  description = "Port du service"
  default     = 80
}

variable "metadata_startup_script" {
  description = "Script de démarrage de la machine virtuelle"
  default     = <<EOF
#!/bin/bash
echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Hello, DevoxxFR!</title>
</head>
<body>
    <h1>Hello, DevoxxFR! 👋</h1>
    <p>Deployed with 💜 by <a href="https://www.hashicorp.com/">Terraform</a>.</p>
</body>
</html>' > index.html
sudo python3 -m http.server ${var.service_port} &
EOF
}

resource "google_compute_network" "demo1network" {
  name                    = "demo1network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "demo1subnet" {
  name          = "demo1subnet"
  ip_cidr_range = "10.0.1.0/24"
  network       = google_compute_network.demo1network.self_link
}

resource "google_compute_firewall" "demo1firewall" {
  name    = "demo1firewall"
  network = google_compute_network.demo1network.self_link

  allow {
    protocol = "tcp"
    ports    = ["22", var.service_port]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = [var.instance_tag]
}

resource "google_compute_instance" "demo1instance" {
  name         = "demo1instance"
  machine_type = var.machine_type
  tags         = [var.instance_tag]

  boot_disk {
    initialize_params {
      image = var.os_image
    }
  }

  network_interface {
    network = google_compute_network.demo1network.id
    subnetwork = google_compute_subnetwork.demo1subnet.id
    access_config {}
  }

  metadata_startup_script = var.metadata_startup_script

  service_account {
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

output "name" {
  value = google_compute_instance.demo1instance.name
}

output "ip" {
  value = google_compute_instance.demo1instance.network_interface.0.access_config.0.nat_ip
}

output "url" {
  value = "http://${google_compute_instance.demo1instance.network_interface.0.access_config.0.nat_ip}:${var.service_port}"
}
