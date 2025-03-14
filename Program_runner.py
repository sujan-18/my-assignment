from decoration import decoration

decoration()
def menu():
    choice= input('Enter your choice from above menu:')
    while True:
        if choice=="1":
            from Login_functions.admin_login import admin_login
            admin_login()
            
        elif choice=="2":
            from Login_functions.manager_login import manager_login
            manager_login()
            
        elif choice=="3":
            from Login_functions.chef_login import chef_login
            chef_login()
        elif choice=="4":
            from Login_functions.customer_login import customer_login
            customer_login()
        elif choice=="5":
            print('Program exit!............')
            exit()
        else:
            print("Enter valid menu from above list.")
            decoration()
            menu()
            
menu()




