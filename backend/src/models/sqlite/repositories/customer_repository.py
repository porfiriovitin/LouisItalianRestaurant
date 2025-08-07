from backend.src.models.sqlite.entities.customers import CustomerTable
from sqlalchemy.orm.exc import NoResultFound

class CustomerRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert_customer(self, customer_name, cpf, cellphone):
        with self.db_connection as database:
            try:
                customer_data = CustomerTable(
                    customer_name = customer_name,
                    cpf = cpf,
                    cellphone = cellphone
                )
                database.session.add(customer_data)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
            
    def get_customer(self, customer_id:int):
        with self.db_connection as database:
            try:
                customer = (
                    database.session
                    .query(CustomerTable)
                    .filter(CustomerTable.customer_id == customer_id)
                    .with_entities(
                        CustomerTable.customer_name,
                        CustomerTable.cpf,
                        CustomerTable.cellphone
                    ).one()
                )
                return customer
            except NoResultFound:
                return None