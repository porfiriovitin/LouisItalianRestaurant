from backend.src.models.sqlite.settings.base import Base
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey

class Tables(Base):
    __tablename__ = "tables"

    table_number = Column(INTEGER, primary_key=True)
    
    def __repr__(self):
        return f"Table number = {self.table_number}"
