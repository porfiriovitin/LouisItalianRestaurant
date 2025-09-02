import re
from src.controllers.reservations.interfaces.list_available_tables import ListAvailableTablesInterface
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError

class ListAvailableTablesController(ListAvailableTablesInterface):

    def __init__(self, reservation_repository: ReservationRepositoryInterface):
        self.__reservation_repository = reservation_repository

    def list_available_tables(self, booking_date: str) -> list:
        if not self._validate_date(booking_date):
            raise HttpBadRequestError("Invalid date format. Please use YYYY-MM-DD.")
        available_tables = self.__reservation_repository.ListAvailableTables(booking_date)
        if not available_tables:
            raise HttpNotFoundError("No available tables found for the specified date.")
        formatted_response = self.__format_response(available_tables)
        return formatted_response

    def _validate_date(self, date: str) -> bool:
        return re.match(r"^\d{4}-\d{2}-\d{2}$", date) is not None

    def __format_response(self, available_tables: list) -> list:
        return {
            "AvailableTables": [
                {
                    "table_number": table["table_number"],
                } for table in available_tables
            ]
        }
