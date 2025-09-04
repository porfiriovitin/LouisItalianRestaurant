from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler
from src.main.routes.customers_routes import customer_route_bp
from src.main.routes.reservation_routes import reservation_route_bp
from src.main.routes.tables_routes import tables_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(customer_route_bp)
app.register_blueprint(reservation_route_bp)
app.register_blueprint(tables_route_bp)
