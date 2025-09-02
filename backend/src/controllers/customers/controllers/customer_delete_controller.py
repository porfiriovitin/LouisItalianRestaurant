from backend.src.models.sqlite.entities.customers import CustomerTable
from backend.src.models.sqlite.interfaces.customer_repository import CustomerRepositoryInterface
from backend.src.controllers.customers.interfaces.customer_delete_controller import CustomerDeleteInterface
from src.errors.error_types.http_not_found import HttpNotFoundError

class CustomerDeleteController(CustomerDeleteInterface):
    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.__customer_repository = customer_repository

    def delete_customer(self, customer_id: int) -> None:
        customer = self.__customer_repository.get_customer_by_id(customer_id)
        if not customer:
            raise HttpNotFoundError(f"Customer with id {customer_id} not found")
        self.__customer_repository.delete_customer(customer_id)
