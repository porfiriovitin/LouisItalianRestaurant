from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def ListAvailableTablesValidator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        booking_date: constr(min_length=10, max_length=10) #type: ignore

    if not isinstance(http_request.body, dict):
        raise HttpUnprocessableEntityError("Request body must be a JSON object.")

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e