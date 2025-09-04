from abc import ABC, abstractmethod

class ReservateTableInterface(ABC):
    @abstractmethod
    def reservate_table(self):
        pass