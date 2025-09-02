from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def customer_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        customer_name: constr(min_length=1) #type: ignore
        cpf: constr(min_length=11, max_length=11) #type: ignore
        cellphone: constr(min_length=10, max_length=15) #type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e