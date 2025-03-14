customer_login_path="data/login_data_customer.txt"
def customer_login():
    print("Enter the email and password before login...")
    attempt=3
    while attempt>0:
        username=input("Enter the username: ").lower()
        password=input("Enter the password: ").lower()
        with open(customer_login_path,'r') as f:
            for line in f:
                user_data=line.strip().split(",")
                if user_data[0] == username and user_data[1] == password:
                    print("Login successful!")
                    from Menu_file.customer_menu import customer_menu
                    customer_menu()
                else:
                    attempt=attempt-1
                    print(f"Now you have {attempt} attempt left")
            if attempt==0:
                print("Maximum attempt try again later!!!!!")
            break

        print("You are back to our home page (:)")
        from decoration import decoration
        
        from Program_runner import menu



