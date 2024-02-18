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

def list_referring_customers():
    converted_customer_name = input("Enter the Converted Customer's name: ")
    referring_customers = get_referring_customers(converted_customer_name)

    if referring_customers:
        print(f"Referring Customers for {converted_customer_name}:")
        for customer in referring_customers:
            print(f"Customer ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")
            leads = get_leads_by_converted_customer(customer)
            if leads:
                print("Associated Leads:")
                for lead in leads:
                    print(f"  Lead ID: {lead.id}, Customer: {lead.customer_name}")
            else:
                print("No associated leads.")
    else:
        print(f"No referring customers found for Converted Customer {converted_customer_name}")

def list_discount_eligible_customers():
    eligible_customers = get_discount_eligible_customers()

    if eligible_customers:
        print("Discount Eligible Customers:")
        for customer in eligible_customers:
            print(f"{customer.first_name} {customer.last_name} is eligible for 20% off their next purchase.")
    else:
        print("No eligible customers found for the discount.")

def get_leads_by_sales_associate(sales_associate_name):
    leads = (
        session.query(Lead)
        .join(SalesAssociate)
        .filter(SalesAssociate.first_name == sales_associate_name)
        .all()
    )
    return leads

def get_referring_customers(converted_customer_name):
    referring_customers = (
        session.query(ConvertedCustomer)
        .filter(ConvertedCustomer.first_name == converted_customer_name)
        .all()
    )
    return referring_customers

def get_leads_by_converted_customer(converted_customer):
    leads = (
        session.query(Lead)
        .filter(Lead.converted_customer == converted_customer)
        .all()
    )
    return leads

def get_discount_eligible_customers():
    eligible_customers = (
        session.query(ConvertedCustomer)
        .filter(ConvertedCustomer.referred_leads_count >= 3)
        .all()
    )
    return eligible_customers