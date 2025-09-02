from abc import ABC, abstractmethod

class CustomerDeleteInterface(ABC):
    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass