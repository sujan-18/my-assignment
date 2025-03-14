# Customer menu
def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. View & Order Food")
        print("2. View Order Status")
        print("3. Send Feedback")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            from Customers_functions.view_order_food import view_and_order_food
            view_and_order_food()
        elif choice == "2":
            from Customers_functions.view_order_status import view_order_status
            view_order_status()
        elif choice == "3":
            from Customers_functions.send_feedback import send_feedback
            send_feedback()
        elif choice == "4":
            from Profile_update_file.update_profile_customer import update_profile
            update_profile()
        elif choice == "5":
            print("You are back to home page...")
            from decoration import decoration
            from Program_runner import menu
            decoration()
            menu()
            break
        else:
            print("Invalid choice. Try again.")



