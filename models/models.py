from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class SalesAssociate(Base):
    __tablename__ = 'sales_associate'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    leads = relationship('Lead', back_populates='sales_associate')

class Lead(Base):
    __tablename__ = 'lead'
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    sales_associate_id = Column(Integer, ForeignKey('sales_associate.id'))
    sales_associate = relationship('SalesAssociate', back_populates='leads')
    converted_customer_id = Column(Integer, ForeignKey('converted_customer.id'))
    converted_customer = relationship('ConvertedCustomer', back_populates='leads')

class ConvertedCustomer(Base):
    __tablename__ = 'converted_customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    leads = relationship('Lead', back_populates='converted_customer')
    referred_leads_count = Column(Integer, default=0)
