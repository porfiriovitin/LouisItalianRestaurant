from backend.src.models.sqlite.entities.customers import CustomerTable
from backend.src.models.sqlite.interfaces.customer_repository import CustomerRepositoryInterface
from backend.src.controllers.customers.interfaces.customer_finder_controller import CustomerFinderControllerInterface
from src.errors.error_types.http_not_found import HttpNotFoundError

class CustomerFinderController(CustomerFinderControllerInterface):
    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.__customer_repository = customer_repository

    def find(self, customer_id):
        customer = self.__find_customer_in_db(customer_id)
        formatted_response = self.__format_response(customer)
        return formatted_response

    def __find_customer_in_db(self, customer_id):
        customer = self.__customer_repository.get_customer_by_id(customer_id)
        if not customer:
            raise HttpNotFoundError("Customer not found")
        return customer
    
    def __format_response(self, customer: CustomerTable) -> dict:
        return {
            "customer_name": customer.customer_name,
            "customer_cpf": customer.cpf,
            "customer_cellphone": customer.cellphone
        }