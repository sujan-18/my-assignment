# Manage menu
MENU_FILE="data/menu.txt"
def manage_menu():
    while True:
        print("\nManage Menu:")
        print("1. Add Menu Item")
        print("2. Edit Menu Item")
        print("3. Delete Menu Item")
        print("4. View Menu")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item name: ")
            price = input("Enter item price: ")
            with open(MENU_FILE, "a") as f:
                f.write(f"{item},{price}\n")
            print("Menu item added successfully!")
        elif choice == "2":
            edit_menu_item()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            view_menu()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def edit_menu_item():
    item = input("Enter item name to edit: ")
    menu_list = []
    with open(MENU_FILE, "r") as f:
        for line in f:
            menu_list.append(line.strip().split(","))
    found = False
    with open(MENU_FILE, "w") as f:
        for menu_item in menu_list:
            if menu_item[0] == item:
                new_price = input("Enter new price: ")
                f.write(f"{menu_item[0]},{new_price}\n")
                print("Menu item updated successfully!")
                found = True
            else:
                f.write(f"{menu_item[0]},{menu_item[1]}\n")
    if not found:
        print("Menu item not found.")

def delete_menu_item():
    item = input("Enter item name to delete: ")
    menu_list = []
    with open(MENU_FILE, "r") as f:
        for line in f:
            menu_list.append(line.strip().split(","))
    found = False
    with open(MENU_FILE, "w") as f:
        for menu_item in menu_list:
            if menu_item[0] != item:
                f.write(f"{menu_item[0]},{menu_item[1]}\n")
            else:
                found = True
    if found:
        print("Menu item deleted successfully!")
    else:
        print("Menu item not found.")

def view_menu():
    print("\nMenu:")
    with open(MENU_FILE, "r") as f:
        for line in f:
            print(line.strip())
