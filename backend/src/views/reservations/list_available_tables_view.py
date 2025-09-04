from src.controllers.reservations.interfaces.list_available_tables_controller import ListAvailableTablesInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface
from src.validators.list_available_tables_validator import ListAvailableTablesValidator

class ListAvailableTablesView(ViewInterface):
    def __init__(self, controller: ListAvailableTablesInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        ListAvailableTablesValidator(http_request)
        booking_date = http_request.body.get("booking_date")
        body_response = self._controller.list_available_tables(booking_date)

        return HttpResponse(status_code=200, body=body_response)