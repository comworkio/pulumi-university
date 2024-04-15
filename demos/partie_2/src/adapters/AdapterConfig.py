import importlib

def get_adapter(type, val):
    class_path = "{}Adapter".format(val.capitalize())
    module = importlib.import_module('adapters.{}.{}'.format(type, class_path))
    return getattr(module, class_path)
