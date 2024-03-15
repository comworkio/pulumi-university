import pulumi
import yaml
from pulumi_google_native.storage import v1 as storage

buckets_yaml_file = "buckets.yaml"

with open(buckets_yaml_file, 'r') as file:
    content_yaml = yaml.safe_load(file)

for bucket in content_yaml['buckets']:
    new_bucket = storage.Bucket(bucket)
