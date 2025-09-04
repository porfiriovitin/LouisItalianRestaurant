import re
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from src.controllers.reservations.interfaces.get_reserved_by_date_controller import GetReservedTablesByDateInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError

class GetReservedTablesByDateController(GetReservedTablesByDateInterface):

    def __init__(self, reservation_repository: ReservationRepositoryInterface):
        self.__reservation_repository = reservation_repository

    def get_reserved_tables(self, date: str) -> list:
        if not self._validate_date(date):
            raise HttpBadRequestError("Invalid date format. Please use YYYY-MM-DD.")
        reserved_tables = self.__reservation_repository.GetReservedTablesByDate(date)
        formatted_response = self.__format_response(reserved_tables)
        return formatted_response

    def _validate_date(self, date: str) -> bool:
        return re.match(r"^\d{4}-\d{2}-\d{2}$", date) is not None
    
    def __format_response(self, reserved_tables: list) -> dict:
        return {  
            "ReservedTables": [
                {
                    "table_number": table["table_number"],
                    "booking_date": table["booking_date"],
                    "scheduled_time": table["scheduled_time"],
                    "customer_id": table["customer_id"]
                } for table in reserved_tables
            ]
        }
