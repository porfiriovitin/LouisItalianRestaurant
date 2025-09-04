from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.reservation_repository import ReservationRepository
from src.controllers.reservations.cancel_reservation_controller import CancelReservationTableController
from src.views.reservations.cancel_reservation_view import CancelReservationView

def CancelReservationComposer() -> CancelReservationView:
    repository = ReservationRepository(db_connection_handler)
    controller = CancelReservationTableController(repository)
    view = CancelReservationView(controller)

    return view
