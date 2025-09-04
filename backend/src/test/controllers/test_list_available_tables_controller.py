import pytest
from unittest.mock import Mock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.controllers.reservations.list_available_tables_controller import ListAvailableTablesController
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError

class TestListAvailableTablesController:
    
    def test_list_available_tables_success(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_table1 = Mock()
        mock_table1.table_number = 1
        mock_table2 = Mock()
        mock_table2.table_number = 3
        mock_repository.ListAvailableTables.return_value = [mock_table1, mock_table2]
        
        controller = ListAvailableTablesController(mock_repository)
        
        # Act
        result = controller.list_available_tables("2024-12-25")
        
        # Assert
        mock_repository.ListAvailableTables.assert_called_once_with("2024-12-25")
        assert "AvailableTables" in result
        assert len(result["AvailableTables"]) == 2
        assert result["AvailableTables"][0]["table_number"] == 1
        assert result["AvailableTables"][1]["table_number"] == 3
    
    def test_list_available_tables_invalid_date_format(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid date format"):
            controller.list_available_tables("25-12-2024")
    
    def test_list_available_tables_invalid_date_format_short(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid date format"):
            controller.list_available_tables("2024-1-1")
    
    def test_list_available_tables_invalid_date_format_with_text(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid date format"):
            controller.list_available_tables("2024-Dec-25")
    
    def test_list_available_tables_no_tables_found(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_repository.ListAvailableTables.return_value = []
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        with pytest.raises(HttpNotFoundError, match="No available tables found"):
            controller.list_available_tables("2024-12-25")
    
    def test_list_available_tables_repository_error(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        mock_repository.ListAvailableTables.side_effect = Exception("Database error")
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            controller.list_available_tables("2024-12-25")
    
    def test_validate_date_valid_format(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        assert controller._validate_date("2024-12-25") == True
        assert controller._validate_date("2023-01-01") == True
        assert controller._validate_date("2025-12-31") == True
    
    def test_validate_date_invalid_format(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ListAvailableTablesController(mock_repository)
        
        # Act & Assert
        assert controller._validate_date("25-12-2024") == False
        assert controller._validate_date("2024-1-1") == False
        assert controller._validate_date("2024-Dec-25") == False
        assert controller._validate_date("invalid") == False
