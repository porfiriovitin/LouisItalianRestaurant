import re
from backend.src.controllers.customers.controllers.customer_lister_controller import CustomerListerController
from backend.src.models.sqlite.interfaces.customer_repository import CustomerRepositoryInterface

class CustomerListerController(CustomerListerController):
    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.__customer_repository = customer_repository

    def list(self)->dict:
        customers = self.__list_customers_on_db()
        formatted_response = self.__format_response(customers=customers)
        return formatted_response

    def __list_customers_on_db(self)->list:
        customers = self.__customer_repository.list_customers()
        return customers
    
    def __format_response(self, customers:list):
        formmated_customers = []
        for customer in customers:
            formmated_customers.append({"name":customer.customer_name, "id": customer.customer_id})

        return {
            "count": len(formmated_customers),
            "customers": formmated_customers
        }