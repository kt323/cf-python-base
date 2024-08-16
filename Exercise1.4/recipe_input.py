import pickle

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    num_ingredients = int(input("Enter the number of ingredients: "))
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    difficulty = calc_difficulty(cooking_time, num_ingredients)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}
    return recipe

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

try:
    filename = input("Enter the filename to open: ")
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {'recipes': [], 'all_ingredients': []}
except Exception as e:
    print("An error occurred:", e)
    data = {'recipes': [], 'all_ingredients': []}

n = int(input("How many recipes would you like to enter? "))
for _ in range(n):
    recipe = take_recipe()
    data['recipes'].append(recipe)
    for ingredient in recipe['ingredients']:
        if ingredient not in data['all_ingredients']:
            data['all_ingredients'].append(ingredient)

try:
    with open('recipebook', 'wb') as file:
        pickle.dump(data, file)
    print("Data saved successfully to 'recipebook'")
except Exception as e:
    print("An error occurred while saving data:", e)