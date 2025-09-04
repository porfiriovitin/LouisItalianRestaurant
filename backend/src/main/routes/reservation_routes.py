from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors
from src.main.composer.reservation.cancel_reservation_composer import CancelReservationComposer
from src.main.composer.reservation.reservate_table_composer import ReservateTableComposer
from src.main.composer.reservation.get_reserved_by_date_composer import GetReservedTablesByDateComposer
from src.main.composer.reservation.list_available_tables_composer import ListAvailableTablesComposer

reservation_route_bp = Blueprint('reservation_route', __name__)

@reservation_route_bp.route('/reservetable', methods=['POST'])
def reservate_table():
    try:
        http_request = HttpRequest(request)
        view = ReservateTableComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@reservation_route_bp.route('/cancelreservation/<int:reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    try:
        http_request = HttpRequest(request, param={'reservation_id': reservation_id})
        view = CancelReservationComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@reservation_route_bp.route('/getreservedtables/<string:date>', methods=['GET'])
def get_reserved_tables_by_date(date):
    try:
        http_request = HttpRequest(request, param={'date': date})
        view = GetReservedTablesByDateComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@reservation_route_bp.route('/listavailabletables', methods=['GET'])
def list_available_tables():
    try:
        http_request = HttpRequest(request)
        view = ListAvailableTablesComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code