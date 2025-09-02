from abc import ABC, abstractmethod

class ListAllTablesInterface(ABC):

    @abstractmethod
    def list_all_tables(self) -> list:
        pass