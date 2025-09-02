from abc import ABC, abstractmethod

class CancelReservationTableInterface(ABC):
    @abstractmethod
    def cancel_reservation(self, reservation_id: str, booking_date: str) -> bool:
        pass
