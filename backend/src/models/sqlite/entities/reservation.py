from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey

class ReservationTable(Base):
    __tablename__ = "reservation"

    reservation_id = Column(INTEGER, primary_key=True)
    table_number = Column(INTEGER, ForeignKey("tables.table_number"))
    booking_date = Column(VARCHAR(10))
    scheduled_time = Column(VARCHAR(8))
    customer_id = Column(INTEGER, ForeignKey("customers.customer_id"))

    def __repr__(self):
        return f"Reservation [Table Number = {self.table_number}, reservation Date = {self.booking_date}, reservation Time = {self.scheduled_time}, customer ID = {self.customer_id}]"