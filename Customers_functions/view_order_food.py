order_food="data/menu.txt"
add_order="data/order_food.txt"
# View and order food
def view_and_order_food():
    print("\nMenu:")
    with open(order_food, "r") as f:
        for line in f:
            print(line.strip())
    item = input("Enter food to order: ")
    quantity = input("Enter quantity: ")
    with open(add_order, "a") as f:
        f.write(f"Item {item}, Quantity {quantity}\n")
    print("Order placed successfully!")