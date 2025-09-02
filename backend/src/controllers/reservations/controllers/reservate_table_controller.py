import re
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from src.controllers.reservations.interfaces.reservate_table_controller import ReservateTableInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError

class ReservationTableController(ReservateTableInterface):

    def __init__(self, reservation_repository: ReservationRepositoryInterface ):
        self.__reservation_repository = reservation_repository

    def book(self, table_info:dict) -> dict:
        table_number = table_info["table_number"],
        booking_date = table_info["booking_date"],
        scheduled_time = table_info["scheduled_time"],
        customer_id = table_info["customer_id"]

        if not self._validate_booking(table_info):
            raise HttpBadRequestError("Invalid table information")
        self._change_table_state_on_db(table_number, booking_date, scheduled_time, customer_id)
        formatted_response = self._format_response(table_info)
        return formatted_response

    def _validate_booking(self, table_info: dict) -> bool:
        if not re.match(r"^\d+$", str(table_info.get("table_number", ""))):
            return False
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", table_info.get("booking_date", "")):
            return False
        if not re.match(r"^\d{2}:\d{2}$", table_info.get("scheduled_time", "")):
            return False
        if not re.match(r"^\d+$", str(table_info.get("customer_id", ""))):
            return False
        return True

    def _change_table_state_on_db(self, table_number, booking_date, scheduled_time, customer_id):
        self.__reservation_repository.BookTable(table_number ,booking_date , scheduled_time, customer_id)

    def _format_response(self, table_info: dict) -> dict:
        return {
            "status": "success",
            "table_number": table_info.get("table_number"),
            "booking_date": table_info.get("booking_date"),
            "scheduled_time": table_info.get("scheduled_time"),
            "customer_id": table_info.get("customer_id"),
        }
