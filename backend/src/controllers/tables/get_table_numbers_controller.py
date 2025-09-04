from src.controllers.tables.interfaces.get_table_numbers import GetTableNumbersInterface
from src.models.sqlite.repositories.tables_repository import TableRepository

class GetTableNumbersController(GetTableNumbersInterface):

    def __init__(self, table_repository: TableRepository):
        self.__table_repository = table_repository

    def GetTableNumbers(self) -> list:
        tables = self.__table_repository.GetTableNumbers()
        return self._format_response(tables)
    
    def _format_response(self, tables: list) -> list:
        return [
            {
                "table": table.table_number,
            }
            for table in tables
        ]
