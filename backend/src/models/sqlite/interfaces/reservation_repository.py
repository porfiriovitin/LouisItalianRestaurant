from abc import ABC, abstractmethod

class ReservationRepositoryInterface(ABC):

    @abstractmethod
    def BookTable(self, table_number, booking_date, scheduled_time, customer_id) -> None:
        pass

    @abstractmethod
    def GetReservedTablesByDate(self, boooking_date: str):
        pass

    @abstractmethod
    def ListAvailableTables(self, booking_date: str):
        pass

    @abstractmethod
    def CancelReservation(self, table_numer: int, booking_date: str) -> None:
        pass