from src.controllers.reservations.interfaces.reservate_table_controller import ReservateTableInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface
from src.validators.reserve_table_validator import ReserveTableValidator

class ReservateTableView(ViewInterface):
    def __init__(self, controller: ReservateTableInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        ReserveTableValidator(http_request)
        reservation_info = http_request.body
        body_response = self._controller.reservate_table(reservation_info)

        return HttpResponse(status_code=201, body=body_response)