from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, SalesAssociate, Lead, ConvertedCustomer

engine = create_engine('sqlite:///crm.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()