from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select

# Connecting SQLAlchemy with the database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Create Declarative Base
Base = declarative_base()

# Define Recipe model
class Recipe(Base):
    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}>"

# Create all defined tables in the database
Base.metadata.create_all(engine)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Define calculate_difficulty function
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# Define insert_recipe function
def insert_recipe(name, ingredients, cooking_time):
    # Calculate the difficulty of the recipe
    difficulty = calculate_difficulty(cooking_time, ingredients)

    # Convert ingredients list to a comma-separated string
    ingredients_string = ", ".join(ingredients)

    # Create a new Recipe instance
    new_recipe = Recipe(name=name, ingredients=ingredients_string, cooking_time=cooking_time, difficulty=difficulty)

    # Add the new recipe to the session
    session.add(new_recipe)

    # Commit the changes
    session.commit()
    print("Recipe added successfully!")

# Define create_recipe function
def create_recipe():
    # Collect recipe details
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time of the recipe (in minutes): "))
    ingredients = input("Enter the ingredients of the recipe (separated by commas): ").split(", ")

    # Insert the recipe into the database
    insert_recipe(name, ingredients, cooking_time)

# Define search_recipe function
def search_recipe():
    # Retrieve all unique ingredients from the Recipes table
    all_ingredients = session.query(func.distinct(Recipe.ingredients)).all()

    # Extract ingredients from the fetched results
    all_ingredients = [ingredient[0] for ingredient in all_ingredients]

    # Display all ingredients to the user with unique numbering
    print("Available ingredients:")
    ingredient_dict = {}
    count = 1
    for ingredients_str in all_ingredients:
        ingredients_list = ingredients_str.split(", ")
        for ingredient in ingredients_list:
            print(f"{count}. {ingredient}")
            ingredient_dict[count] = ingredient
            count += 1

    # Prompt user to select an ingredient to search for
    ingredient_index = int(input("Enter the number corresponding to the ingredient you want to search for: "))
    search_ingredient = ingredient_dict.get(ingredient_index)

    # Prepare and execute SQL query to search for recipes containing the specified ingredient
    search_results = session.query(Recipe).filter(Recipe.ingredients.like(f"%{search_ingredient}%")).all()

    # Display search results to the user
    print("\nSearch Results:")
    if search_results:
        for result in search_results:
            print("Name:", result.name)
            print("Ingredients:", result.ingredients)
            print("Cooking Time:", result.cooking_time, "minutes")
            print("Difficulty:", result.difficulty)
            print()
    else:
        print("No recipes found containing", search_ingredient)


# Define update_recipe function
def update_recipe():
    # Fetch all recipes from the database and list them to the user
    recipes = session.query(Recipe).all()
    print("Available Recipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe.name}")

    # Prompt user to select a recipe to update
    recipe_index = int(input("Enter the index of the recipe you want to update: ")) - 1

    # Check if the recipe with the given index exists
    if 0 <= recipe_index < len(recipes):
        recipe = recipes[recipe_index]

        # Prompt user to select the column to update
        print("Columns available for update: name, cooking_time, ingredients")
        column = input("Enter the column to be updated: ")

        # Prompt user for the new value
        new_value = input("Enter the new value: ")

        # Convert the new value to integer if updating cooking_time
        if column == 'cooking_time':
            new_value = int(new_value)

        # Update the specified column
        setattr(recipe, column, new_value)

        # Recalculate difficulty if updating cooking_time or ingredients
        if column == 'cooking_time' or column == 'ingredients':
            recipe.difficulty = calculate_difficulty(recipe.cooking_time, recipe.ingredients.split(", "))

        # Commit the changes
        session.commit()
        print("Recipe updated successfully!")
    else:
        print("Error: Recipe not found.")

# Define delete_recipe function
def delete_recipe():
    # Fetch all recipes from the database and list them to the user
    recipes = session.query(Recipe).all()
    print("Available Recipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe.name}")

    # Prompt user to select a recipe for deletion
    recipe_index = int(input("Enter the index of the recipe you want to delete: ")) - 1

    # Check if the provided recipe index is valid
    if 0 <= recipe_index < len(recipes):
        recipe = recipes[recipe_index]

        # Delete the specified recipe
        session.delete(recipe)

        # Commit the changes
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Error: Invalid recipe index.")




# Define main_menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_recipe()
        elif choice == '2':
            search_recipe()
        elif choice == '3':
            update_recipe()
        elif choice == '4':
            delete_recipe()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the session before exiting
    session.close()
    print("Session closed.")

# Call the main_menu function
main_menu()