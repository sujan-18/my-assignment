view_sales_path="Data/sales_data.txt"
def view_sales_report():
    print("-"*77)
    print('+-'*12 + "WELCOME TO OUR SALES REPORT PAGE" + '+-'*12)
    print("-"*77)
    print("Choose any option for viewing sales reports:")
    print("1. By Month")
    print("2. By Chef")
    print("3. View All Sales")
    print("4. Go back to admin menu")
    print("=" * 77)

    choice = input( "Enter your choice: ")

    f=open(view_sales_path, "r")
    sales_data = f.readlines() 

    if choice == "1":
        month = input("Enter the month (e.g., January): " ).capitalize()
        print( f"Sales report for {month}:")
        found = False
        for line in  sales_data:
            if month in line:
                print(line.strip())
                view_sales_report()
                found = True
            if not found:
                print(f"No sales data found for {month}.")
                view_sales_report()

    elif choice == "2":
            chef = input("Enter the chef's name (e.g., Chef A): ").capitalize()
            print(f"Sales report for {chef}:")
            found = False
            for line in sales_data:
                if chef in line:
                    print(line.strip())
                    view_sales_report()
                    found = True
            if not found:
                print(f"No sales data found for {chef}.")
                view_sales_report()

    elif choice == "3":
            print("Complete Sales Report:")
            for line in sales_data:
                print(line.strip())
                view_sales_report()
            
    elif choice=="4":
        print(" You are in admin menu ")
        from Menu_file.admin_menu import admin_menu
        admin_menu()


    else:
            print("Invalid choice! Please select a valid option.")
            view_sales_report()
