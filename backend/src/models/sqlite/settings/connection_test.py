from connection import db_connection_handler
from sqlalchemy import text

# :: Connect to db.
db_connection_handler.connect_to_db()

# :: Verify if the engine were created.
engine = db_connection_handler.get_engine()
if engine:
    print("Connected sucessfully!")
else:
    print("Failed creating the engine")

# Agora tente abrir uma sessão e executar algo simples
try:
    with db_connection_handler as db:
        result = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        tables = result.fetchall()
        print("Tables on db: ", tables)
except Exception as e:
    print("Error: ", e)
