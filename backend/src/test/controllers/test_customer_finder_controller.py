import pytest
from unittest.mock import Mock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.controllers.customers.customer_finder_controller import CustomerFinderController
from src.errors.error_types.http_not_found import HttpNotFoundError

class TestCustomerFinderController:
    
    def test_find_customer_success(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_customer = Mock()
        mock_customer.customer_name = "John Doe"
        mock_customer.cpf = "12345678901"
        mock_customer.cellphone = "11987654321"
        
        mock_repository.get_customer_by_id.return_value = mock_customer
        controller = CustomerFinderController(mock_repository)
        
        # Act
        result = controller.find(1)
        
        # Assert
        mock_repository.get_customer_by_id.assert_called_once_with(1)
        assert result["customer_name"] == "John Doe"
        assert result["customer_cpf"] == "12345678901"
        assert result["customer_cellphone"] == "11987654321"
    
    def test_find_customer_not_found(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_repository.get_customer_by_id.return_value = None
        controller = CustomerFinderController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpNotFoundError, match="Customer not found"):
            controller.find(999)
    
    def test_find_customer_with_zero_id(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_repository.get_customer_by_id.return_value = None
        controller = CustomerFinderController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpNotFoundError, match="Customer not found"):
            controller.find(0)
    
    def test_find_customer_with_negative_id(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_repository.get_customer_by_id.return_value = None
        controller = CustomerFinderController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpNotFoundError, match="Customer not found"):
            controller.find(-1)
    
    def test_find_customer_repository_error(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_repository.get_customer_by_id.side_effect = Exception("Database connection failed")
        controller = CustomerFinderController(mock_repository)
        
        # Act & Assert
        with pytest.raises(Exception, match="Database connection failed"):
            controller.find(1)
