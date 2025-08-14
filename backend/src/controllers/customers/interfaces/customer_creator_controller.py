from abc import ABC, abstractmethod

class CustomerCreatorInterface(ABC):
    @abstractmethod
    def create(self, customer_info:dict) -> dict:
        pass