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
    converted_customer_name = input("Enter the Converted Customer's first name: ")
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

def create_lead():
    customer_name = input("Enter customer name: ")
    first_name = input("Enter lead's first name: ")
    last_name = input("Enter lead's last name: ")
    sales_associate_id = int(input("Enter Sales Associate ID for assignment: "))

    lead = Lead(customer_name=customer_name, first_name=first_name, last_name=last_name, sales_associate_id=sales_associate_id)
    session.add(lead)
    session.commit()
    print("Lead created successfully.")

def create_sales_associate():
    first_name = input("Enter Sales Associate's first name: ")
    last_name = input("Enter Sales Associate's last name: ")

    sales_associate = SalesAssociate(first_name=first_name, last_name=last_name)
    session.add(sales_associate)
    session.commit()
    print("Sales Associate created successfully.")

def create_converted_customer():
    first_name = input("Enter Converted Customer's first name: ")
    last_name = input("Enter Converted Customer's last name: ")
    lead_id = int(input("Enter Lead ID for referral: "))

    converted_customer = ConvertedCustomer(first_name=first_name, last_name=last_name, referred_leads_count=0)
    
    # Update referral count for the converted customer
    lead = session.query(Lead).get(lead_id)
    if lead:
        converted_customer.leads.append(lead)
        lead.converted_customer = converted_customer
        converted_customer.referred_leads_count += 1
    
        session.add_all([converted_customer, lead])
        session.commit()
        print("Converted Customer created successfully.")
    else:
        print(f"Lead with ID {lead_id} not found.")

def change_sales_associate_name():
    sales_associate_id = int(input("Enter Sales Associate ID: "))
    new_first_name = input("Enter new first name: ")
    new_last_name = input("Enter new last name: ")

    sales_associate = session.query(SalesAssociate).get(sales_associate_id)
    
    if sales_associate:
        sales_associate.first_name = new_first_name
        sales_associate.last_name = new_last_name
        session.commit()
        print(f"Sales Associate with ID {sales_associate_id} updated successfully.")
    else:
        print(f"Sales Associate with ID {sales_associate_id} not found.")

def delete_lead():
    lead_id = int(input("Enter Lead ID to delete: "))
    lead = session.query(Lead).get(lead_id)

    if lead:
        converted_customer = lead.converted_customer
        if converted_customer:
            converted_customer.referred_leads_count -= 1
            session.delete(lead)
            session.commit()
            print(f"Lead with ID {lead_id} deleted successfully. Referral count reduced for Converted Customer.")
        else:
            print(f"Lead with ID {lead_id} is not associated with any Converted Customer.")
    else:
        print(f"Lead with ID {lead_id} not found.")