class Recipe:
    all_ingredients = []

    def __init__(self, name, cooking_time):
        self._name = name
        self._cooking_time = cooking_time
        self._ingredients = []
        self._difficulty = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value):
        self._cooking_time = value

    def add_ingredients(self, *ingredients):
        self._ingredients.extend(ingredients)
        self.update_all_ingredients()

    @property
    def ingredients(self):
        return self._ingredients

    def calculate_difficulty(self):
        if self._cooking_time < 10 and len(self._ingredients) < 4:
            self._difficulty = "Easy"
        elif self._cooking_time < 10 and len(self._ingredients) >= 4:
            self._difficulty = "Medium"
        elif self._cooking_time >= 10 and len(self._ingredients) < 4:
            self._difficulty = "Intermediate"
        else:
            self._difficulty = "Hard"

    @property
    def difficulty(self):
        if self._difficulty is None:
            self.calculate_difficulty()
        return self._difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients

    def update_all_ingredients(self):
        for ingredient in self._ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        return f"Recipe: {self._name}\nCooking Time (min): {self._cooking_time}\nIngredients: {', '.join(self._ingredients)}\nDifficulty level: {self.difficulty}\n"


def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Creating recipe objects
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")

# List of recipes
recipes_list = [tea, coffee, cake, banana_smoothie]

# Searching for recipes containing specific ingredients
ingredients_to_search = ["Water", "Sugar", "Bananas"]
for ingredient in ingredients_to_search:
    print(f"Recipes containing {ingredient}:")
    recipe_search(recipes_list, ingredient)