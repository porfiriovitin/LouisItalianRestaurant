from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.tables_repository import TableRepository
from src.controllers.tables.get_table_numbers_controller import GetTableNumbersController
from src.views.tables.get_table_numbers_view import GetTableNumbersView

def GetTablesNumberComposer() -> GetTableNumbersView:
    repository = TableRepository(db_connection_handler)
    controller = GetTableNumbersController(repository)
    view = GetTableNumbersView(controller)

    return view
