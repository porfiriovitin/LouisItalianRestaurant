from abc import ABC, abstractmethod

class ReservateTableInterface(ABC):
    @abstractmethod
    def book(self):
        pass