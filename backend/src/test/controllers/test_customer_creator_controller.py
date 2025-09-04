import pytest
from unittest.mock import Mock, patch
from datetime import datetime
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.controllers.customers.customer_creator_controller import CustomerCreatorController
from src.errors.error_types.http_bad_request import HttpBadRequestError

class TestCustomerCreatorController:
    
    def test_create_customer_success(self, mock_db_connection, sample_customer_data):
        # Arrange
        mock_repository = Mock()
        controller = CustomerCreatorController(mock_repository)
        
        # Act
        with patch('src.controllers.customers.customer_creator_controller.datetime') as mock_datetime:
            mock_datetime.utcnow.return_value.strftime.return_value = "25/12/2024 10:30:00"
            result = controller.create(sample_customer_data)
        
        # Assert
        mock_repository.insert_customer.assert_called_once_with(
            "John Doe", "12345678901", "11987654321"
        )
        assert "Customer registered" in result
        assert result["Customer registered"]["name"] == "John Doe"
        assert result["Customer registered"]["date"] == "25/12/2024 10:30:00"
    
    def test_create_customer_with_missing_name(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = CustomerCreatorController(mock_repository)
        invalid_data = {
            "cpf": "12345678901",
            "cellphone": "11987654321"
        }
        
        # Act & Assert
        with pytest.raises(KeyError):
            controller.create(invalid_data)
    
    def test_create_customer_with_missing_cpf(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = CustomerCreatorController(mock_repository)
        invalid_data = {
            "customer_name": "John Doe",
            "cellphone": "11987654321"
        }
        
        # Act & Assert
        with pytest.raises(KeyError):
            controller.create(invalid_data)
    
    def test_create_customer_with_missing_cellphone(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = CustomerCreatorController(mock_repository)
        invalid_data = {
            "customer_name": "John Doe",
            "cpf": "12345678901"
        }
        
        # Act & Assert
        with pytest.raises(KeyError):
            controller.create(invalid_data)
    
    def test_create_customer_repository_error(self, mock_db_connection, sample_customer_data):
        # Arrange
        mock_repository = Mock()
        mock_repository.insert_customer.side_effect = Exception("Database error")
        controller = CustomerCreatorController(mock_repository)
        
        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            controller.create(sample_customer_data)
