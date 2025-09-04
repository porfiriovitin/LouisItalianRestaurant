from abc import ABC, abstractmethod

class GetReservedTablesByDateInterface(ABC):
    @abstractmethod
    def get_reserved_tables(self, date: str) -> list:
        pass
