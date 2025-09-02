from backend.src.controllers.tables.interfaces.list_all_tables_controller import ListAllTablesInterface
from src.models.sqlite.repositories.tables_repository import TableRepository

class ListAllTablesController(ListAllTablesInterface):

    def __init__(self, table_repository: TableRepository):
        self.__table_repository = table_repository

    def _list_all_tables(self) -> list:
        tables = self.__table_repository.list_all_tables()
        return self._format_response(tables)
    
    def _format_response(self, tables: list) -> list:
        return [
            {
                "number": table["number"],
            }
            for table in tables
        ]
