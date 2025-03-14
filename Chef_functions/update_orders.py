order_food_path="data/order_food.txt"
def update_order_status():
    print("\nUpdate Order Status:")
    order_id = input("Enter the order ID to update: ").capitalize
    new_status = input("Enter new status (e.g., 'In Progress', 'Completed'): ")
    orders = []
    with open(order_food_path, "r") as f:
        for line in f:
            orders.append(line.strip().split(","))
    found = False
    with open(order_food_path, "w") as f:
        for order in orders:
            if order[0] == order_id:
                f.write(f"{order[0]},{order[1]},{new_status}\n")
                print(f"Order {order_id} status updated to {new_status}.")
                found = True
            else:
                f.write(f"{order[0]},{order[1]},{order[2]}\n")
    if not found:
        print("Order not found.")