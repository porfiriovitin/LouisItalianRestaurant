from abc import ABC, abstractmethod
from backend.src.models.sqlite.entities.tables import Tables

class TableInterface(ABC):
    
    @abstractmethod
    def ListTables(self) -> list[Tables]:
        pass
