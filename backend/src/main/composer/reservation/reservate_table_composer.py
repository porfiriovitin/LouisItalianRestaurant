from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.reservation_repository import ReservationRepository
from src.controllers.reservations.reservate_table_controller import ReservateTableController
from src.views.reservations.reservate_table_view import ReservateTableView

def ReservateTableComposer() -> ReservateTableView:
    repository = ReservationRepository(db_connection_handler)
    controller = ReservateTableController(repository)
    view = ReservateTableView(controller)

    return view