import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.views.customers.customer_creator_view import CustomerCreatorView
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class TestCustomerCreatorView:
    
    def test_handle_success(self, sample_customer_data):
        # Arrange
        mock_controller = Mock()
        mock_controller.create.return_value = {
            "Customer registered": {
                "name": "John Doe",
                "date": "25/12/2024 10:30:00"
            }
        }
        
        view = CustomerCreatorView(mock_controller)
        
        # Mock request with valid data
        mock_request = Mock()
        mock_request.get_json.return_value = sample_customer_data
        http_request = HttpRequest(mock_request)
        
        # Act
        with patch('src.views.customers.customer_creator_view.customer_creator_validator'):
            response = view.handle(http_request)
        
        # Assert
        mock_controller.create.assert_called_once_with(sample_customer_data)
        assert response.status_code == 201
        assert "Customer registered" in response.body
        assert response.body["Customer registered"]["name"] == "John Doe"
    
    def test_handle_validation_error(self, sample_customer_data):
        # Arrange
        mock_controller = Mock()
        view = CustomerCreatorView(mock_controller)
        
        mock_request = Mock()
        mock_request.get_json.return_value = {"invalid": "data"}
        http_request = HttpRequest(mock_request)
        
        # Act & Assert
        with patch('src.views.customers.customer_creator_view.customer_creator_validator', 
                         side_effect=HttpUnprocessableEntityError("Validation error")):
            with pytest.raises(HttpUnprocessableEntityError):
                view.handle(http_request)
    
    def test_handle_controller_error(self, sample_customer_data):
        # Arrange
        mock_controller = Mock()
        mock_controller.create.side_effect = Exception("Controller error")
        view = CustomerCreatorView(mock_controller)
        
        mock_request = Mock()
        mock_request.get_json.return_value = sample_customer_data
        http_request = HttpRequest(mock_request)
        
        # Act & Assert
        with patch('src.views.customers.customer_creator_view.customer_creator_validator'):
            with pytest.raises(Exception, match="Controller error"):
                view.handle(http_request)
    
    def test_handle_with_dict_body(self, sample_customer_data):
        # Arrange
        mock_controller = Mock()
        mock_controller.create.return_value = {
            "Customer registered": {
                "name": "John Doe",
                "date": "25/12/2024 10:30:00"
            }
        }
        view = CustomerCreatorView(mock_controller)
        
        # Create HttpRequest directly with dict (not Flask request)
        http_request = HttpRequest(sample_customer_data)
        
        # Act
        with patch('src.views.customers.customer_creator_view.customer_creator_validator'):
            response = view.handle(http_request)
        
        # Assert
        mock_controller.create.assert_called_once_with(sample_customer_data)
        assert response.status_code == 201
        assert response.body["Customer registered"]["name"] == "John Doe"
