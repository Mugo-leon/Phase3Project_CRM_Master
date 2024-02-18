from cli import list_leads, list_referring_customers, list_discount_eligible_customers

def main():
    print("Welcome to CRM Master!")
    while True:
        print("Options:")
        print("1. List leads by Sales Associate")
        print("2. List referring customers")
        print("3. List discount eligible customers")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            list_leads()
        elif choice == '2':
            list_referring_customers()
        elif choice == '3':
            list_discount_eligible_customers()
        elif choice == '4':
            print("Exiting CRM Master. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()