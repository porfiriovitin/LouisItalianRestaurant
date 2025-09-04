from src.controllers.reservations.interfaces.cancel_reservation_controller import CancelReservationTableInterface
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError

class CancelReservationTableController(CancelReservationTableInterface):

    def __init__(self, reservation_repository: ReservationRepositoryInterface):
        self.__reservation_repository = reservation_repository

    def cancel_reservation(self, reservation_id: str, booking_date: str) -> bool:
        self.__reservation_repository.CancelReservation(reservation_id, booking_date)
        return "Reservation cancelled successfully."

    