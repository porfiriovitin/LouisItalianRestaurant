from src.controllers.customers.interfaces.customer_delete_controller import CustomerDeleteInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class CustomerDeleteView(ViewInterface):
    def __init__(self, controller:CustomerDeleteInterface):
        self._controller = controller

    def handle(self, http_request:HttpRequest) -> HttpResponse:
        customer_id = http_request.param["customer_id"]
        self._controller.delete_customer(customer_id)

        return HttpResponse(status_code=204, body={})
