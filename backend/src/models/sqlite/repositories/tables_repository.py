from src.models.sqlite.entities.tables import Tables
from src.models.sqlite.interfaces.tables_repository import TableInterface
from sqlalchemy.orm.exc import NoResultFound

class TableRepository(TableInterface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def GetTableNumbers(self) -> list[Tables]:
        with self.__db_connection as database:
            try:
                tables = database.session.query(Tables).all()
                return tables
            except NoResultFound:
                return "No tables found"