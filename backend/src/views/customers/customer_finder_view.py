from src.controllers.customers.interfaces.customer_finder_controller import CustomerFinderControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class CustomerFinderView(ViewInterface):
    def __init__(self, controller:CustomerFinderControllerInterface):
        self._controller = controller

    def handle(self, http_request:HttpRequest) -> HttpResponse:
        customer_id = http_request.param["customer_id"]
        body_response = self._controller.find(customer_id)

        return HttpResponse(status_code=200, body=body_response)