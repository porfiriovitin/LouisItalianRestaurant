from backend.src.models.sqlite.settings.base import Base
from sqlalchemy import Column, VARCHAR, INTEGER

class CustomerTable(Base):
    __tablename__ = "customers"

    customer_id = Column(INTEGER, primary_key=True)
    customer_name = Column(VARCHAR(100), nullable=False)
    cpf = Column(VARCHAR(13), nullable=False)
    cellphone = Column(VARCHAR(15), nullable=False)

    def __repr__(self):
        return f"Customer [Name = {self.customer_name}, cpf = {self.cpf}, cellphone = {self.cellphone}]"