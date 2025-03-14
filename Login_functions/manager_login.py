manager_login_path="data/login_data_manager.txt"
def manager_login():
    print("Enter the email/username and password before login...")
    attempt=3
    while attempt>0:
        username=input("Enter the username: ").lower()
        password=input("Enter the password: ").lower()

        with open(manager_login_path,'r') as f:
            for line in f:
                user_data=line.strip().split(",")
                if user_data[0] == username and user_data[1] == password:
                    print("Login successful!")
                    from Menu_file.manager_menu import manager_menu
                    manager_menu()
             
                else:
                    attempt=attempt-1
                    print(f"Now you have {attempt} attempt left")
            if attempt==0:
                print("Maximum attempt try again later!!!!!")
                break
        print("You are back to our home page (:)")
        from decoration import decoration
        
        from Program_runner import menu
                

                




