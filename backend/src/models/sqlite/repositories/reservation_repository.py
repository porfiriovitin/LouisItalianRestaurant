from src.models.sqlite.entities.reservation import ReservationTable
from src.models.sqlite.entities.tables import Tables
from src.models.sqlite.interfaces.reservation_repository import ReservationRepositoryInterface
from sqlalchemy.orm.exc import NoResultFound


class ReservationRepository(ReservationRepositoryInterface):
    def __init__(self, db__connection):
        self.__db_connection = db__connection

    def BookTable(self, table_number, booking_date, scheduled_time, customer_id):
        with self.__db_connection as database:
            try:
                reservation_data = ReservationTable(
                    table_number=table_number,
                    booking_date=booking_date,
                    scheduled_time=scheduled_time,
                    customer_id=customer_id,
                )
                database.session.add(reservation_data)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

    def GetReservedTablesByDate(self, boooking_date: str):
        with self.__db_connection as database:
            try:
                reservations = (
                    database.session.query(ReservationTable)
                    .filter(boooking_date == boooking_date)
                    .with_entities(
                        ReservationTable.table_number,
                        ReservationTable.customer_id,
                        ReservationTable.scheduled_time,
                    )
                    .all()
                )
                return reservations
            except NoResultFound:
                return "There's no booked table on this date"

    def ListAvailableTables(self, booking_date: str):
        with self.__db_connection as database:
            try:
                reserved_tables_subquery = database.session.query(
                    ReservationTable.table_number
                ).filter(ReservationTable.booking_date == booking_date)
                available_tables = (
                    database.session.query(Tables)
                    .filter(~Tables.table_number.in_(reserved_tables_subquery))
                    .all()
                )
                return available_tables
            except NoResultFound:
                return "No available tables found"

    def CancelReservation(self, table_numer: int, booking_date: str):
        with self.__db_connection as database:
            try:
                database.session.query(ReservationTable).filter(
                    ReservationTable.table_number == table_numer
                    and ReservationTable.booking_date == booking_date
                ).delete()
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e("Can't delete, reserved table not found")
