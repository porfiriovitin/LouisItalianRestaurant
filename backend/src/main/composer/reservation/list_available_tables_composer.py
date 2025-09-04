from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.reservation_repository import ReservationRepository
from src.controllers.reservations.list_available_tables_controller import ListAvailableTablesController
from src.views.reservations.list_available_tables_view import ListAvailableTablesView

def ListAvailableTablesComposer() -> ListAvailableTablesView:
    repository = ReservationRepository(db_connection_handler)
    controller = ListAvailableTablesController(repository)
    view = ListAvailableTablesView(controller)

    return view