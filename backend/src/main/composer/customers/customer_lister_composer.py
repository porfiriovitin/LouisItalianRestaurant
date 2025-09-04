from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.customer_repository import CustomerRepository
from src.controllers.customers.customer_lister_controller import CustomerListerController
from src.views.customers.customer_lister_view import CustomerListerView

def CustomerListerComposer() -> CustomerListerView:
    repository = CustomerRepository(db_connection_handler)
    controller = CustomerListerController(repository)
    view = CustomerListerView(controller)

    return view