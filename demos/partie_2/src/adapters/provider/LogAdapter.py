from adapters.provider.ProviderAdapter import ProviderAdapter
from utils.size import get_enum_value
from utils.logger import log_msg

class LogAdapter(ProviderAdapter):
    def size_to_type(self, size):
        return "e2-medium"

    def create_instance(self, name, project, region, zone, size):
        vmtype = self.size_to_type(size)
        log_msg("INFO", "[LogAdapter][create_instance] name = {}, project = {}, region = {}, zone = {}, vmtype = {}".format(name, project, region, zone, vmtype))
        return {
            'status': 'ok'
        }
