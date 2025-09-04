from src.models.sqlite.interfaces.customer_repository import CustomerRepositoryInterface
from src.controllers.customers.interfaces.customer_creator_controller import CustomerCreatorInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError
from datetime import datetime

class CustomerCreatorController(CustomerCreatorInterface):
    def __init__(self, customer_repository: CustomerRepositoryInterface):
        self.__customer_repository = customer_repository

    def create(self, customer_info:dict) -> dict:
        customer_name = customer_info["customer_name"]
        cpf = customer_info ["cpf"]
        cellphone = customer_info["cellphone"]
        self.__insert_customer_in_db(customer_name, cpf, cellphone)
        formatted_response = self.__format_response(customer_info)
        return formatted_response

    def __insert_customer_in_db(self, customer_name, cpf, cellphone):
        self.__customer_repository.insert_customer(customer_name, cpf, cellphone)

    def __format_response(self, customer_info:dict) -> dict:
        return{
            "Customer registered":{
                "name": customer_info["customer_name"],
                "date": datetime.utcnow().strftime('%d/%m/%Y %H:%M:%S')
            }
        }
        
        
    