customer_login_path="data/login_data_customer.txt"

# Update profile functionality
def update_profile():
    print("\nUpdate Profile:")
    username = input("Enter your current username: ")
    password = input("Enter your current password: ")

    # Read all users
    users = []
    with open(customer_login_path, "r") as f:
        for line in f:
            users.append(line.strip().split(","))

    # Find the user
    found = False
    for user in users:
        if user[0] == username and user[1] == password:
            found = True
            print(f"Current Username: {user[0]}")
            print(f"Current Password: {user[1]}")
            new_username = input("Enter new username (leave blank to keep current): ")
            new_password = input("Enter new password (leave blank to keep current): ")

            # Update username and password if provided
            if new_username:
                user[0] = new_username
            if new_password:
                user[1] = new_password
            print("Profile updated successfully!")
            break

    if not found:
        print("Invalid username or password. Profile update failed.")

    # Write updated users back to the file
    with open(customer_login_path, "w") as f:
        for user in users:
            f.write(f"{user[0]},{user[1]}\n")
