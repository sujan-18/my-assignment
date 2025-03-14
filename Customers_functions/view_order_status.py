# View order status
order_food_path="data/order_food.txt"
def view_order_status():
    print("\nOrder Status:")
    with open(order_food_path, "r") as f:
        for line in f:
            print(line.strip())
