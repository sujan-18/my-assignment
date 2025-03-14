
def admin_menu():
    print("-"*77)
    print('+-'*12 + "WELCOME TO OUR ADMIN PAGE" + '+-'*12)
    print("-"*77)
    print("Here are some role of Administrator:")
    print("1. Manage Staff\n2. View Sales report\n3. View Feedback\n4. Update own profile\n5. Back to menu")
    while True:
        choice=int(input("Enter your choice from admin role:"))
        if choice==1:
            from Admin_functions.manage_staff import manage_staff
            manage_staff()
        elif choice==2:
            from Admin_functions.view_report import view_sales_report
            view_sales_report()
        elif choice==3:
            from Admin_functions.view_feedback import view_feedback
            view_feedback()
        elif choice==4:
            from Profile_update_file.update_profile_admin import update_profile
            update_profile()
        elif choice==5:
            from decoration import decoration
            decoration()
            from Program_runner import menu
            menu()
            
        else:
            print("Your Choice Is Out Of Range!!")


