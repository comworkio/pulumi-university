from fastapi import FastAPI

from restful_ressources import import_ressources

version = "unkown"

app = FastAPI(
    docs_url="/",
    title="Pulumi university API Documentation",
    version = "0.1",
    description="Official pulumi university API Swagger documentation"
)

import_ressources(app)
