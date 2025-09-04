import pytest
from unittest.mock import Mock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.controllers.reservations.reservate_table_controller import ReservateTableController
from src.errors.error_types.http_bad_request import HttpBadRequestError

class TestReservateTableController:
    
    def test_reservate_table_success(self, mock_db_connection, sample_reservation_data):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        
        # Act
        result = controller.reservate_table(sample_reservation_data)
        
        # Assert
        mock_repository.BookTable.assert_called_once_with(
            1, "2024-12-25", "19:30", 1
        )
        assert result["status"] == "success"
        assert result["table_number"] == 1
        assert result["booking_date"] == "2024-12-25"
        assert result["scheduled_time"] == "19:30"
        assert result["customer_id"] == 1
    
    def test_reservate_table_invalid_table_number_negative(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": -1,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid table number"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_invalid_table_number_zero(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": 0,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid table number"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_invalid_table_number_string(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": "1",
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid table number"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_invalid_date_format(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": 1,
            "booking_date": "25-12-2024",  # Wrong format
            "scheduled_time": "19:30",
            "customer_id": 1
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid booking date format"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_invalid_time_format(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "7:30 PM",  # Wrong format
            "customer_id": 1
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid scheduled time format"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_invalid_customer_id_negative(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": -1
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid customer ID"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_invalid_customer_id_zero(self, mock_db_connection):
        # Arrange
        mock_repository = Mock()
        controller = ReservateTableController(mock_repository)
        invalid_data = {
            "table_number": 1,
            "booking_date": "2024-12-25",
            "scheduled_time": "19:30",
            "customer_id": 0
        }
        
        # Act & Assert
        with pytest.raises(HttpBadRequestError, match="Invalid customer ID"):
            controller.reservate_table(invalid_data)
    
    def test_reservate_table_repository_error(self, mock_db_connection, sample_reservation_data):
        # Arrange
        mock_repository = Mock()
        mock_repository.BookTable.side_effect = Exception("Database error")
        controller = ReservateTableController(mock_repository)
        
        # Act & Assert
        with pytest.raises(Exception, match="Database error"):
            controller.reservate_table(sample_reservation_data)
