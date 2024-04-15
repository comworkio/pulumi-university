from routes import api_health as health, api_instance as instance

health_check_routes = ['/health', '/v1/health']
instances_routes = ['/instance', '/v1/instance']

def import_ressources(app):
    for route in health_check_routes:
        app.include_router(health.router, tags=["Health"], prefix=route)

    for route in instances_routes:
        app.include_router(instance.router, tags=["Instance"], prefix=route)
