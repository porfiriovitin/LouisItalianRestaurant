from abc import ABC, abstractmethod
from src.models.sqlite.entities.tables import Tables

class TableInterface(ABC):
    
    @abstractmethod
    def GetTableNumbers(self) -> list[Tables]:
        pass
