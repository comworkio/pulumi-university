import pulumi
from pulumi_google_native.storage import v1 as storage

# Partie 1
bucket = storage.Bucket('my-bucket')
