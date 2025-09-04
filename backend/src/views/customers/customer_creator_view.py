from src.controllers.customers.interfaces.customer_creator_controller import CustomerCreatorInterface
from src.validators.customer_creator_validator import customer_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class CustomerCreatorView(ViewInterface):
    def __init__(self, controller: CustomerCreatorInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        customer_creator_validator(http_request)
        customer_info = http_request.body
        body_response = self._controller.create(customer_info)

        return HttpResponse(status_code=201, body=body_response)