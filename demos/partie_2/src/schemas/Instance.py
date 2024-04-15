from schemas.Resource import PulumiResource

class Instance(PulumiResource):
    region: str = "europe-west1"
    zone: str = "b"
    size: str = "xl"
