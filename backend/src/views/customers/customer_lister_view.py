from src.controllers.customers.interfaces.customer_lister_controller import CustomerListerControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class CustomerListerView(ViewInterface):
    def __init__(self, controller: CustomerListerControllerInterface):
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        customers = self._controller.list()

        return HttpResponse(status_code=200, body=customers)
