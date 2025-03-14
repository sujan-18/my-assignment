INGREDIENTS_FILE="data/request_ingredients.txt"
# View ingredients list
def view_ingredients_list():
    print("\nIngredients List:")
    with open(INGREDIENTS_FILE, "r") as f:
        for line in f:
            print(line.strip())