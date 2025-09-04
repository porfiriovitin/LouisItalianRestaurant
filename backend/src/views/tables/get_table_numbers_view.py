from src.controllers.tables.interfaces.get_table_numbers import GetTableNumbersInterface
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class GetTableNumbersView(ViewInterface):

    def __init__(self, controller: GetTableNumbersInterface):
        self.__controller = controller

    def handle(self, http_request) -> HttpResponse:
        table_numbers = self.__controller.GetTableNumbers()
        return HttpResponse(status_code=200, body=table_numbers)
