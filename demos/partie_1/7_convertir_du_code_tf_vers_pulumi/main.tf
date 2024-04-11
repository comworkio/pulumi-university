provider "google" {
  project = "<YOUR_GOOGLE_PROJECT_ID>"
  region  = "us-central1"  # Update with your desired region
}

resource "google_storage_bucket" "my_bucket" {
  name     = "my-bucket"
  location = "US"  # Update with your desired location

  # Uncomment the following block if you want to specify storage class
  # storage_class = "REGIONAL"

  # Uncomment the following block if you want to enable versioning
  # versioning {
  #   enabled = true
  # }
}

output "bucket_self_link" {
  value = google_storage_bucket.my_bucket.self_link
}
