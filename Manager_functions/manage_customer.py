# Manage customers
CUSTOMERS_FILE="data/customer_data.txt"
def manage_customers():
    while True:
        print("\nManage Customers:")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. View Customers")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            with open(CUSTOMERS_FILE, "a") as f:
                f.write(f"{name},{email}\n")
            print("Customer added successfully!")
        elif choice == "2":
            edit_customer()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            view_customers()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def edit_customer():
    name = input("Enter customer name to edit: ")
    customers = []
    with open(CUSTOMERS_FILE, "r") as f:
        for line in f:
            customers.append(line.strip().split(","))
    found = False
    with open(CUSTOMERS_FILE, "w") as f:
        for customer in customers:
            if customer[0] == name:
                new_email = input("Enter new email: ")
                f.write(f"{customer[0]},{new_email}\n")
                print("Customer updated successfully!")
                found = True
            else:
                f.write(f"{customer[0]},{customer[1]}\n")
    if not found:
        print("Customer not found.")

def delete_customer():
    name = input("Enter customer name to delete: ")
    customers = []
    with open(CUSTOMERS_FILE, "r") as f:
        for line in f:
            customers.append(line.strip().split(","))
    found = False
    with open(CUSTOMERS_FILE, "w") as f:
        for customer in customers:
            if customer[0] != name:
                f.write(f"{customer[0]},{customer[1]}\n")
            else:
                found = True
    if found:
        print("Customer deleted successfully!")
    else:
        print("Customer not found.")

def view_customers():
    print("\nCustomer List:")
    with open(CUSTOMERS_FILE, "r") as f:
        for line in f:
            print(line.strip())
