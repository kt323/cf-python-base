import pickle

recipes_list = [
    {
        "name": "Scrambled Eggs",
        "cooking_time": 5,
        "ingredients": ["Eggs", "Salt", "Pepper"],
        "difficulty": "Easy"
    },
    # Add more recipes here
]

all_ingredients = set()
for recipe in recipes_list:
    all_ingredients.update(recipe['ingredients'])

data = {
    "recipes_list": recipes_list,
    "all_ingredients": list(all_ingredients)
}

with open('recipebook', 'wb') as file:
    pickle.dump(data, file)

print("Recipe data has been saved to 'recipebook'")