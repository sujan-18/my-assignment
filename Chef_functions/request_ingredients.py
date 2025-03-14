INGREDIENTS_FILE="data/request_ingredients.txt"
def request_ingredients():
    ingredient = input("Enter ingredient name: ")
    quantity = input("Enter quantity: ")
    with open(INGREDIENTS_FILE, "a") as f:
        f.write(f"{ingredient},{quantity}\n")
    print("Ingredient request added successfully!")