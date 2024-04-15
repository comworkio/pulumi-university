from pydantic import BaseModel
from typing import Optional

class PulumiResource(BaseModel):
    name: str = "instance1"
    project: str = "MyProject"
    provider: str = "gcp"
    asynchronous: Optional[bool] = True
