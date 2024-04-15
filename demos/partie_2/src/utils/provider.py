from enum import Enum

Provider = Enum('Provider', ['gcp', 'log'])

def get_enum_value(name):
    try:
        return Provider[name.lower()]
    except KeyError:
        return None

def is_valid_provider(name):
    return None != get_enum_value(name)

def is_not_valid_provider(name):
    return not is_valid_provider(name)
