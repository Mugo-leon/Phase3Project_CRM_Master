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
    sales_assoc1 = SalesAssociate(first_name='Leon', last_name='Muriuki')
    sales_assoc2 = SalesAssociate(first_name='Olive', last_name='Kirigo')
    session.add_all([sales_assoc1, sales_assoc2])
    session.commit()

    # Create converted customers
    converted_cust1 = ConvertedCustomer(first_name='Loice', last_name='Njambi', referred_leads_count=0)
    converted_cust2 = ConvertedCustomer(first_name='Wanjiru', last_name='Ndegwa', referred_leads_count=0)
    session.add_all([converted_cust1, converted_cust2])
    session.commit()

    # Create leads and associate with converted customers and sales associates
    lead1 = Lead(customer_name='Ruth Mutonyi',first_name='Ruth', last_name='Mutonyi', sales_associate=sales_assoc1, converted_customer=converted_cust1)
    lead2 = Lead(customer_name='Kennedy Sigei',first_name='Kennedy', last_name='Sigei', sales_associate=sales_assoc2, converted_customer=converted_cust1)
    lead3 = Lead(customer_name='Alice Mwangi',first_name='Alice', last_name='Mwangi', sales_associate=sales_assoc1, converted_customer=converted_cust2)
    lead4 = Lead(customer_name='Cecily Kariuki',first_name='Cecily', last_name='Kariuki', sales_associate=sales_assoc2, converted_customer=converted_cust1)
    session.add_all([lead1, lead2, lead3, lead4])

    # Dynamically update referred_leads_count for customers
    update_referred_leads_count()

def update_referred_leads_count():
    # Fetch all converted customers
    converted_customers = session.query(ConvertedCustomer).all()

    # Update referred_leads_count based on the leads associated with each customer
    for customer in converted_customers:
        customer.referred_leads_count = len(customer.leads)
        
    session.commit()

if __name__ == '__main__':
    seed_data()