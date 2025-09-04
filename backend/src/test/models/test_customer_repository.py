import pytest
from unittest.mock import Mock, MagicMock
from sqlalchemy.orm.exc import NoResultFound
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.models.sqlite.repositories.customer_repository import CustomerRepository
from src.models.sqlite.entities.customers import CustomerTable

class TestCustomerRepository:
    
    def test_insert_customer_success(self, mock_db_connection):
        # Arrange
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        repository.insert_customer("John Doe", "12345678901", "11987654321")
        
        # Assert
        mock_db_connection.session.add.assert_called_once()
        mock_db_connection.session.commit.assert_called_once()
        
        # Check if CustomerTable was created with correct data
        call_args = mock_db_connection.session.add.call_args[0][0]
        assert call_args.customer_name == "John Doe"
        assert call_args.cpf == "12345678901"
        assert call_args.cellphone == "11987654321"
    
    def test_insert_customer_rollback_on_error(self, mock_db_connection):
        # Arrange
        mock_db_connection.session.add.side_effect = Exception("Database error")
        repository = CustomerRepository(mock_db_connection)
        
        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            repository.insert_customer("John Doe", "12345678901", "11987654321")
        
        mock_db_connection.session.rollback.assert_called_once()
        mock_db_connection.session.commit.assert_not_called()
    
    def test_get_customer_by_id_success(self, mock_db_connection):
        # Arrange
        mock_customer = Mock()
        mock_customer.customer_name = "John Doe"
        mock_customer.cpf = "12345678901"
        mock_customer.cellphone = "11987654321"
        
        # Setup the query chain
        mock_query = Mock()
        mock_filter = Mock()
        mock_with_entities = Mock()
        
        mock_db_connection.session.query.return_value = mock_query
        mock_query.filter.return_value = mock_filter
        mock_filter.with_entities.return_value = mock_with_entities
        mock_with_entities.one.return_value = mock_customer
        
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        result = repository.get_customer_by_id(1)
        
        # Assert
        assert result == mock_customer
        mock_db_connection.session.query.assert_called_with(CustomerTable)
        mock_query.filter.assert_called_once()
        mock_filter.with_entities.assert_called_once()
        mock_with_entities.one.assert_called_once()
    
    def test_get_customer_by_id_not_found(self, mock_db_connection):
        # Arrange
        mock_query = Mock()
        mock_filter = Mock()
        mock_with_entities = Mock()
        
        mock_db_connection.session.query.return_value = mock_query
        mock_query.filter.return_value = mock_filter
        mock_filter.with_entities.return_value = mock_with_entities
        mock_with_entities.one.side_effect = NoResultFound()
        
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        result = repository.get_customer_by_id(999)
        
        # Assert
        assert result is None
    
    def test_list_customers_success(self, mock_db_connection):
        # Arrange
        mock_customers = [Mock(), Mock()]
        mock_db_connection.session.query.return_value.all.return_value = mock_customers
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        result = repository.list_customers()
        
        # Assert
        assert result == mock_customers
        mock_db_connection.session.query.assert_called_with(CustomerTable)
    
    def test_list_customers_no_result(self, mock_db_connection):
        # Arrange
        mock_db_connection.session.query.return_value.all.side_effect = NoResultFound()
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        result = repository.list_customers()
        
        # Assert
        assert result == "No customers found"
    
    def test_delete_customer_success(self, mock_db_connection):
        # Arrange
        mock_customer = Mock()
        mock_query = Mock()
        mock_filter = Mock()
        
        mock_db_connection.session.query.return_value = mock_query
        mock_query.filter.return_value = mock_filter
        mock_filter.one.return_value = mock_customer
        
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        repository.delete_customer(1)
        
        # Assert
        mock_db_connection.session.delete.assert_called_once_with(mock_customer)
        mock_db_connection.session.commit.assert_called_once()
    
    def test_delete_customer_not_found(self, mock_db_connection):
        # Arrange
        mock_query = Mock()
        mock_filter = Mock()
        
        mock_db_connection.session.query.return_value = mock_query
        mock_query.filter.return_value = mock_filter
        mock_filter.one.side_effect = NoResultFound()
        
        repository = CustomerRepository(mock_db_connection)
        
        # Act
        result = repository.delete_customer(999)
        
        # Assert
        assert result is None
        mock_db_connection.session.delete.assert_not_called()
        mock_db_connection.session.commit.assert_not_called()
    
    def test_delete_customer_database_error(self, mock_db_connection):
        # Arrange
        mock_query = Mock()
        mock_filter = Mock()
        mock_filter.one.side_effect = Exception("Database connection failed")
        
        mock_db_connection.session.query.return_value = mock_query
        mock_query.filter.return_value = mock_filter
        
        repository = CustomerRepository(mock_db_connection)
        
        # Act & Assert
        with pytest.raises(Exception, match="Database connection failed"):
            repository.delete_customer(1)
