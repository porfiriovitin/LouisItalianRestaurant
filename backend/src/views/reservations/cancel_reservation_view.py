from src.controllers.reservations.interfaces.cancel_reservation_controller import CancelReservationTableInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class CancelReservationView(ViewInterface):
    def __init__(self, controller: CancelReservationTableInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        reservation_id = http_request.param.get("reservation_id")
        booking_date = http_request.body.get("booking_date") if http_request.body else None
        result = self._controller.cancel_reservation(reservation_id, booking_date)
        return HttpResponse(status_code=200, body={"message": result})