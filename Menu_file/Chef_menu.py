# Chef functionalities
def chef_menu():
    while True:
        print("\nChef Menu:")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. Request Ingredients")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            from Chef_functions.view_orders import view_orders
            view_orders()
        elif choice == "2":
            from Chef_functions.update_orders import update_order_status
            update_order_status()
        elif choice == "3":
            from Chef_functions.request_ingredients import request_ingredients
            request_ingredients()
        elif choice == "4":
            from Profile_update_file.update_profile_chef import update_profile
            update_profile()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

