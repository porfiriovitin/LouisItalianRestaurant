from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.customer_repository import CustomerRepository
from src.controllers.customers.customer_creator_controller import CustomerCreatorController
from src.views.customers.customer_creator_view import CustomerCreatorView

def CustomerCreatorComposer() -> CustomerCreatorView:
    repository = CustomerRepository(db_connection_handler)
    controller = CustomerCreatorController(repository)
    view = CustomerCreatorView(controller)

    return view