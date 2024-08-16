import pickle

def display_recipe(recipe):
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print(f"Difficulty level: {recipe['difficulty']}")

def search_ingredient(data):
    all_ingredients = data['all_ingredients']
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
    with open('recipebook', 'rb') as file:
        data = pickle.load(file)
    search_ingredient(data)
except FileNotFoundError:
    print("File 'recipebook' not found.")
except EOFError:
    print("The file is empty or corrupted.")
except Exception as e:
    print(f"An error occurred: {e}")