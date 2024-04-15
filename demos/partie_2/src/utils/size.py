from enum import Enum

Size = Enum('Size', ['XL', 'L', 'M', 'S'])

def get_enum_value(name):
    try:
        return Size[name.upper()]
    except KeyError:
        return None

def is_valid_size(name):
    return None != get_enum_value(name)

def is_not_valid_size(name):
    return not is_valid_size(name)
