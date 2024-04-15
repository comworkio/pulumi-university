from abc import ABC, abstractmethod

class ProviderAdapter(ABC):
    @abstractmethod
    def size_to_type(self, size):
        pass

    @abstractmethod
    def create_instance(self, name, project, region, zone, size):
        pass
