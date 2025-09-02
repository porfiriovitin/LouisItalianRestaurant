from backend.src.models.sqlite.entities.customers import CustomerTable
from backend.src.models.sqlite.interfaces.customer_repository import CustomerRepositoryInterface
from sqlalchemy.orm.exc import NoResultFound

class CustomerRepository(CustomerRepositoryInterface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_customer(self, customer_name, cpf, cellphone):
        with self.__db_connection as database:
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
            
    def get_customer_by_id(self, customer_id:int):
        with self.__db_connection as database:
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
    
    def list_customers(self):
        with self.__db_connection as database:
            try:
                customers = database.session.query(CustomerTable).all()
                return customers
            except NoResultFound:
                return "No customers found"
            
    def delete_customer(self, customer_id:int):
        with self.__db_connection as database:
            try:
                customer = (
                    database.session
                    .query(CustomerTable)
                    .filter(CustomerTable.customer_id == customer_id)
                    .one()
                )
                database.session.delete(customer)
                database.session.commit()
            except NoResultFound:
                return None