import pickle

def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print(f"Difficulty level: {recipe['difficulty']}")

def search_ingredient(data):
    all_ingredients = set()
    for recipe in data["recipes"]:
        all_ingredients.update(recipe['ingredients'])
    
    all_ingredients = list(all_ingredients)
    
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i+1}. {ingredient}")
    
    try:
        choice = int(input("Enter the number corresponding to the ingredient you want to search: "))
        ingredient_searched = all_ingredients[choice - 1]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return
    
    found_recipes = [recipe for recipe in data["recipes"] if ingredient_searched in recipe['ingredients']]
    
    if found_recipes:
        print(f"Recipes containing {ingredient_searched}:")
        for recipe in found_recipes:
            display_recipe(recipe)
    else:
        print(f"No recipes found containing {ingredient_searched}.")

try:
    filename = input("Enter the filename that contains your recipe data: ")
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found.")
except EOFError:
    print("The file is empty or corrupted.")
else:
    search_ingredient(data)
