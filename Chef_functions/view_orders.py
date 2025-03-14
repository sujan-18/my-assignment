order_food_path="data/order_food.txt"
def view_orders():
    print("\nCustomer Orders:")
    with open(order_food_path, "r") as f:
        for line in f:
            print(line.strip().split(","))
          