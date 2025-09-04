import re
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from src.controllers.reservations.interfaces.reservate_table_controller import ReservateTableInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError

class ReservateTableController(ReservateTableInterface):

    def __init__(self, reservation_repository: ReservationRepositoryInterface ):
        self.__reservation_repository = reservation_repository

    def reservate_table(self, table_info:dict) -> dict:
        table_number = table_info["table_number"]
        booking_date = table_info["booking_date"]
        scheduled_time = table_info["scheduled_time"]
        customer_id = table_info["customer_id"]

        self._validate(table_info)
        self._change_table_state_on_db(table_number, booking_date, scheduled_time, customer_id)
        formatted_response = self._format_response(table_info)
        return formatted_response

    def _validate(self, table_info: dict):
        if not isinstance(table_info.get("table_number"), int) or table_info.get("table_number") <= 0:
            raise HttpBadRequestError("Invalid table number. It must be a positive integer.")

        date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(date_pattern, table_info.get("booking_date", "")):
            raise HttpBadRequestError("Invalid booking date format. It must be YYYY-MM-DD.")

        time_pattern = r"^\d{2}:\d{2}$"
        if not re.match(time_pattern, table_info.get("scheduled_time", "")):
            raise HttpBadRequestError("Invalid scheduled time format. It must be HH:MM.")

        if not isinstance(table_info.get("customer_id"), int) or table_info.get("customer_id") <= 0:
            raise HttpBadRequestError("Invalid customer ID. It must be a positive integer.")

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
