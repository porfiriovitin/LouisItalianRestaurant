import pytest
from unittest.mock import Mock
from pydantic import ValidationError
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.validators.customer_creator_validator import customer_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class TestCustomerCreatorValidator:
    
    def test_valid_customer_data(self, sample_customer_data):
        # Arrange
        mock_request = Mock()
        mock_request.get_json.return_value = sample_customer_data
        http_request = HttpRequest(mock_request)
        
        # Act & Assert (should not raise exception)
        customer_creator_validator(http_request)
    
    def test_valid_customer_data_with_dict(self, sample_customer_data):
        # Arrange
        http_request = HttpRequest(sample_customer_data)
        
        # Act & Assert (should not raise exception)
        customer_creator_validator(http_request)
    
    def test_invalid_body_type_string(self):
        # Arrange
        http_request = HttpRequest("not a dict")
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError, match="Request body must be a JSON object"):
            customer_creator_validator(http_request)
    
    def test_invalid_body_type_list(self):
        # Arrange
        http_request = HttpRequest([1, 2, 3])
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError, match="Request body must be a JSON object"):
            customer_creator_validator(http_request)
    
    def test_invalid_body_type_none(self):
        # Arrange
        mock_request = Mock()
        mock_request.get_json.return_value = None
        http_request = HttpRequest(mock_request)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError, match="Request body must be a JSON object"):
            customer_creator_validator(http_request)
    
    def test_missing_customer_name(self):
        # Arrange
        incomplete_data = {
            "cpf": "12345678901",
            "cellphone": "11987654321"
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            customer_creator_validator(http_request)
    
    def test_missing_cpf(self):
        # Arrange
        incomplete_data = {
            "customer_name": "John Doe",
            "cellphone": "11987654321"
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            customer_creator_validator(http_request)
    
    def test_missing_cellphone(self):
        # Arrange
        incomplete_data = {
            "customer_name": "John Doe",
            "cpf": "12345678901"
        }
        http_request = HttpRequest(incomplete_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            customer_creator_validator(http_request)
    
    def test_empty_customer_name(self):
        # Arrange
        invalid_data = {
            "customer_name": "",  # Empty name
            "cpf": "12345678901",
            "cellphone": "11987654321"
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            customer_creator_validator(http_request)
    
    def test_short_cpf(self):
        # Arrange
        invalid_data = {
            "customer_name": "John Doe",
            "cpf": "123456789",  # Too short
            "cellphone": "11987654321"
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            customer_creator_validator(http_request)
    
    def test_short_cellphone(self):
        # Arrange
        invalid_data = {
            "customer_name": "John Doe",
            "cpf": "12345678901",
            "cellphone": "119876543"  # Too short
        }
        http_request = HttpRequest(invalid_data)
        
        # Act & Assert
        with pytest.raises(HttpUnprocessableEntityError):
            customer_creator_validator(http_request)
    
    def test_extra_fields_allowed(self):
        # Arrange
        data_with_extra = {
            "customer_name": "John Doe",
            "cpf": "12345678901",
            "cellphone": "11987654321",
            "extra_field": "should be ignored"
        }
        http_request = HttpRequest(data_with_extra)
        
        # Act & Assert (should not raise exception)
        customer_creator_validator(http_request)
