from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, SalesAssociate, Lead, ConvertedCustomer

engine = create_engine('sqlite:///crm.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    # Check if data already exists
    if session.query(SalesAssociate).count() > 0:
        print("Seed data already exists. Skipping.")
        return

    # Create sales associates
    sales_assoc1 = SalesAssociate(first_name='John', last_name='Doe')
    sales_assoc2 = SalesAssociate(first_name='Jane', last_name='Smith')
    session.add_all([sales_assoc1, sales_assoc2])
    session.commit()

    # Create converted customers
    converted_cust1 = ConvertedCustomer(first_name='Alice', last_name='Johnson', referred_leads_count=0)
    converted_cust2 = ConvertedCustomer(first_name='Bob', last_name='Williams', referred_leads_count=0)
    session.add_all([converted_cust1, converted_cust2])
    session.commit()

    # Create leads and associate with converted customers and sales associates
    lead1 = Lead(customer_name='Lead 1', first_name='Lead1FirstName', last_name='Lead1LastName', sales_associate=sales_assoc1, converted_customer=converted_cust1)
    lead2 = Lead(customer_name='Lead 2', first_name='Lead2FirstName', last_name='Lead2LastName', sales_associate=sales_assoc2, converted_customer=converted_cust1)
    lead3 = Lead(customer_name='Lead 3', first_name='Lead3FirstName', last_name='Lead3LastName', sales_associate=sales_assoc1, converted_customer=converted_cust2)
    lead4 = Lead(customer_name='Lead 4', first_name='Lead4FirstName', last_name='Lead4LastName', sales_associate=sales_assoc2, converted_customer=converted_cust1)
    session.add_all([lead1, lead2, lead3, lead4])

    # Dynamically update referred_leads_count for customers
    update_referred_leads_count()