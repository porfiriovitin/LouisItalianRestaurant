from abc import ABC, abstractmethod

class CustomerFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, customer_id):
        pass