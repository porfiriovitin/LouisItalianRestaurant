from backend.src.models.sqlite.entities.tables import Tables
from sqlalchemy.orm.exc import NoResultFound

class TableRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def ListTables(self) -> list[Tables]:
        with self.__db_connection as database:
            try:
                tables = database.session.query(Tables).all()
                return tables
            except NoResultFound:
                return "No tables found"