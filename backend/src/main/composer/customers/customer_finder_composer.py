from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.customer_repository import CustomerRepository
from src.controllers.customers.customer_finder_controller import CustomerFinderController
from src.views.customers.customer_finder_view import CustomerFinderView

def CustomerFinderComposer() -> CustomerFinderView:
    repository = CustomerRepository(db_connection_handler)
    controller = CustomerFinderController(repository)
    view = CustomerFinderView(controller)

    return view
