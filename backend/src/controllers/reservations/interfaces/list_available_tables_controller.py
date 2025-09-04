from abc import ABC, abstractmethod

class ListAvailableTablesInterface(ABC):
    @abstractmethod
    def list_available_tables(self, booking_date: str) -> list:
        pass
