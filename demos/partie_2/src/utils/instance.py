from adapters.AdapterConfig import get_adapter

def new_instance(name, project, region, zone, size, provider):
    provider_adapter = get_adapter('provider', provider)
    return provider_adapter().create_instance(name, project, region, zone, size)
