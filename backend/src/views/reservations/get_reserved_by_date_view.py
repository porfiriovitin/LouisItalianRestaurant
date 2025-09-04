from src.controllers.reservations.interfaces.get_reserved_by_date_controller import GetReservedTablesByDateInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class GetReservedTablesByDateView(ViewInterface):
    def __init__(self, controller: GetReservedTablesByDateInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        date_info = http_request.body
        body_response = self._controller.get_reserved_tables_by_date(date_info)

        return HttpResponse(status_code=200, body=body_response)