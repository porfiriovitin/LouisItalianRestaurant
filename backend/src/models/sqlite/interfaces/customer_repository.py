from abc import ABC, abstractmethod
from src.models.sqlite.entities.customers import CustomerTable

class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def insert_customer(self, customer_name, cpf, cellphone) -> None:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id:int) -> CustomerTable:
        pass

    def list_customers(self):
        pass