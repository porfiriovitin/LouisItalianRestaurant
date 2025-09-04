from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def ReserveTableValidator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        table_number: int #type: ignore
        booking_date: constr(min_length=10, max_length=10) #type: ignore
        scheduled_time: constr(min_length=5, max_length=5) #type: ignore
        customer_id: int #type: ignore

    if not isinstance(http_request.body, dict):
        raise HttpUnprocessableEntityError("Request body must be a JSON object.")

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e