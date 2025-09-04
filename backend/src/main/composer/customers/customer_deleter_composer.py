from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.customer_repository import CustomerRepository
from src.controllers.customers.customer_delete_controller import CustomerDeleteController
from src.views.customers.customer_deleter_view import  CustomerDeleteView

def CustomerDeleterComposer() -> CustomerDeleteView:
    repository = CustomerRepository(db_connection_handler)
    controller = CustomerDeleteController(repository)
    view = CustomerDeleteView(controller)

    return view
