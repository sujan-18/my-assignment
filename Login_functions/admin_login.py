#import admin_menu

login_path='Data/login_data_admin.txt'
def admin_login():
    print('+-'*12 + "ENTER DETAILS FOR LOGIN" + '+-'*12)
    attempt=3
    while attempt > 0:
        name=input("Enter your name: ").lower()
        user_name=input('Enter your user_name: ').lower()
        password=input('Enter your password: ').lower()
        file=open(login_path,'r')
        for path in file:
            role,user,pwd=path.strip().split(',')
            if user_name==user and password==pwd: 
                print(f"Welcome, {name}..! Your role is {role}.")
                from Menu_file.admin_menu import admin_menu
                admin_menu()
                return True
            else:
                attempt=attempt-1
                print(f"wrong login credentials. Remaining attempt{attempt}")
                
                #return False
        if attempt==0   :
           print("To many wrong attempt!!!Page Exiting..... " )
           break
    print("You are back to our home page (:)")
    from decoration import decoration
    
    from Program_runner import menu
'''result = admin_login()
print(result)
if result:
    print("login success")
else:
    print("failed")'''


