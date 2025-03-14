# Manager menu
def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Manage Customers")
        print("2. Manage Menu")
        print("3. View Ingredients List")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            from Manager_functions.manage_customer import manage_customers
            manage_customers()
        elif choice == "2":
            from Manager_functions.manage_menu import manage_menu
            manage_menu()
        elif choice == "3":
            from Manager_functions.view_ingredients import view_ingredients_list
            view_ingredients_list()
        elif choice == "4":
            from Profile_update_file.update_profile_manager import update_profile
            update_profile()
        elif choice == "5":
            print("You are back to home page...")
            from decoration import decoration
            from Program_runner import menu
            decoration()
            menu()
            

       
        else:
            print("Invalid choice. Try again.")


