from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors
from src.main.composer.tables.get_tables_number_composer import GetTablesNumberComposer

tables_route_bp = Blueprint('tables_route', __name__)

@tables_route_bp.route('/gettablenumbers', methods=['GET'])
def get_table_numbers():
    try:
        http_request = HttpRequest(request)
        view = GetTablesNumberComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code
