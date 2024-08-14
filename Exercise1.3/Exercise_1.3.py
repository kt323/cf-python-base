recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    num_ingredients = int(input("Enter the number of ingredients: "))
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

n = int(input("How many recipes would you like to enter? "))

for _ in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)

for recipe in recipes_list:
    num_ingredients = len(recipe['ingredients'])
    if recipe['cooking_time'] < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif recipe['cooking_time'] < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif recipe['cooking_time'] >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print(f"Difficulty level: {difficulty}")
    print()

print("\nIngredients Available Across All Recipes")
print("----------------------------------------")
sorted_ingredients = sorted(set(ingredients_list))
for ingredient in sorted_ingredients:
    print(ingredient)