from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.reservation_repository import ReservationRepository
from src.controllers.reservations.get_reservated_by_date_controller import GetReservedTablesByDateController
from src.views.reservations.get_reserved_by_date_view import GetReservedTablesByDateView

def GetReservedTablesByDateComposer() -> GetReservedTablesByDateView:
    repository = ReservationRepository(db_connection_handler)
    controller = GetReservedTablesByDateController(repository)
    view = GetReservedTablesByDateView(controller)

    return view