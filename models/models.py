from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class SalesAssociate(Base):
    __tablename__ = 'sales_associate'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    leads = relationship('Lead', back_populates='sales_associate')