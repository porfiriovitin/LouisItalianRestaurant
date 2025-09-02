import re
from src.controllers.reservations.interfaces.cancel_reservation_table import CancelReservationTableInterface
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError

class CancelReservationTableController(CancelReservationTableInterface):

    def __init__(self, reservation_repository: ReservationRepositoryInterface):
        self.__reservation_repository = reservation_repository

    def _cancel_reservation(self, reservation_id: str, booking_date: str) -> bool:
        self.__reservation_repository.CancelReservation(reservation_id, booking_date)
        self._validate_cancellation(reservation_id, booking_date)
        formatted_response = self._format_reservation_data(reservation_id, booking_date)
        return formatted_response

    def _validate_cancellation(self, reservation_id: str, booking_date: str) -> bool:
        non_valid_characters = re.compile(r"[^\w-]")
        if non_valid_characters.search(reservation_id) or non_valid_characters.search(booking_date):
            raise HttpBadRequestError("Invalid characters in reservation ID or booking date.")
        return True

    def _format_reservation_data(self, reservation_id: str, booking_date: str) -> dict:
        return {
            "reservation_id": reservation_id,
            "booking_date": booking_date
        }
