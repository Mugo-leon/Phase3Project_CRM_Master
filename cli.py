from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, SalesAssociate, Lead, ConvertedCustomer

engine = create_engine('sqlite:///crm.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

def list_leads():
    sales_associate_name = input("Enter the Sales Associate's name: ")
    leads = get_leads_by_sales_associate(sales_associate_name)
    
    if leads:
        print(f"Leads assigned to {sales_associate_name}:")
        for lead in leads:
            print(f"Lead ID: {lead.id}, Customer: {lead.customer_name}")
    else:
        print(f"No leads found for Sales Associate {sales_associate_name}")