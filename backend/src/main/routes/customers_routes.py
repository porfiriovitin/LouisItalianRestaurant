from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors
from src.main.composer.customers.customer_creator_composer import CustomerCreatorComposer
from src.main.composer.customers.customer_deleter_composer import CustomerDeleterComposer
from src.main.composer.customers.customer_finder_composer import CustomerFinderComposer
from src.main.composer.customers.customer_lister_composer import CustomerListerComposer

customer_route_bp = Blueprint('customer_route', __name__)

@customer_route_bp.route('/createcustomer', methods=['POST'])
def create_customer():
    try:
        http_request = HttpRequest(request)
        view = CustomerCreatorComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@customer_route_bp.route('/deletecustomer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        http_request = HttpRequest(request, param={'customer_id': customer_id})
        view = CustomerDeleterComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@customer_route_bp.route('/findcustomer/<int:customer_id>', methods=['GET'])
def find_customer(customer_id):
    try:
        http_request = HttpRequest(request, param={'customer_id': customer_id})
        view = CustomerFinderComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code

@customer_route_bp.route('/listcustomers', methods=['GET'])
def list_customers():
    try:
        http_request = HttpRequest(request)
        view = CustomerListerComposer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as error:
        http_response = handle_errors(error)
        return jsonify(http_response.body), http_response.status_code