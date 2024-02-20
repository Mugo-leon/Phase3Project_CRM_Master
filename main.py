from cli import list_leads, list_referring_customers, list_discount_eligible_customers, create_lead, create_sales_associate, create_converted_customer, change_sales_associate_name, delete_lead

def main():
    print("Welcome to CRM Master!")
    while True:
        print("Options:")
        print("1. List leads by Sales Associate")
        print("2. List referring customers")
        print("3. List discount eligible customers")
        print("4. Create a lead")
        print("5. Create a sales associate")
        print("6. Create a converted customer")
        print("7. Change the name of a sales associate")
        print("8. Delete a lead")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            list_leads()
        elif choice == '2':
            list_referring_customers()
        elif choice == '3':
            list_discount_eligible_customers()
        elif choice == '4':
            create_lead()
        elif choice == '5':
            create_sales_associate()
        elif choice == '6':
            create_converted_customer()
        elif choice == '7':
            change_sales_associate_name()
        elif choice == '8':
            delete_lead()
        elif choice == '9':
            print("Exiting CRM Master. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == '__main__':
    main()
