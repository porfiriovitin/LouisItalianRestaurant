from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    '''Logic for Db Connection'''
    def __init__(self):
        self.__connection_string = "sqlite:///backend/database.db"
        self.__engine = None 
        self.session = None 

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = DBConnectionHandler()

'''
Usage example:

with db_connection_handler as db:
    result = db.session.execute("SELECT * FROM customer_table")  # exemplo
    for row in result:
        print(row)
'''