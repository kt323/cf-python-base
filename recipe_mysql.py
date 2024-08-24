import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

# Initialize cursor object
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Switch to the specified database
cursor.execute("USE task_database")

# Create the table Recipes if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
""")

# Define calculate_difficulty function
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    
    return difficulty

# Define insert_recipe function
def insert_recipe(conn, cursor, name, ingredients, cooking_time):
    # Calculate the difficulty of the recipe
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert ingredients list to a comma-separated string
    ingredients_string = ", ".join(ingredients)
    
    # Prepare the SQL query
    query = """
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
    """
    values = (name, ingredients_string, cooking_time, difficulty)
    
    # Execute the query
    cursor.execute(query, values)
    
    # Commit the changes
    conn.commit()

# Define create_recipe function
def create_recipe(conn, cursor):
    # Collect recipe details
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time of the recipe (in minutes): "))
    ingredients = input("Enter the ingredients of the recipe (separated by commas): ").split(", ")
    
    # Calculate the difficulty of the recipe
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert ingredients list to a comma-separated string
    ingredients_string = ", ".join(ingredients)
    
    # Prepare the SQL query
    query = """
        INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
        VALUES (%s, %s, %s, %s)
    """
    values = (name, ingredients_string, cooking_time, difficulty)
    
    # Execute the query
    cursor.execute(query, values)
    
    # Commit the changes
    conn.commit()
    print("Recipe added successfully!")

# Define search_recipe function
def search_recipe(conn, cursor):
    # Retrieve all unique ingredients from the Recipes table
    cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
    results = cursor.fetchall()

    # Extract ingredients from the fetched results
    all_ingredients = []
    for row in results:
        ingredient = row[0]
        ingredients_list = ingredient.split(", ")
        all_ingredients.extend(ingredients_list)

    # Remove duplicates and sort the ingredients list
    all_ingredients = sorted(set(all_ingredients))

    # Display all ingredients to the user
    print("Available ingredients:")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f"{index}. {ingredient}")

    # Prompt user to select an ingredient to search for
    ingredient_index = int(input("Enter the number corresponding to the ingredient you want to search for: "))
    search_ingredient = all_ingredients[ingredient_index - 1]

    # Prepare and execute SQL query to search for recipes containing the specified ingredient
    query = """
        SELECT name, ingredients, cooking_time, difficulty
        FROM Recipes
        WHERE ingredients LIKE %s
    """
    cursor.execute(query, ("%" + search_ingredient + "%",))
    search_results = cursor.fetchall()

    # Display search results to the user
    print("\nSearch Results:")
    if search_results:
        for result in search_results:
            print("Name:", result[0])
            print("Ingredients:", result[1])
            print("Cooking Time:", result[2], "minutes")
            print("Difficulty:", result[3])
            print()
    else:
        print("No recipes found containing", search_ingredient)

# Define update_recipe function
def update_recipe(conn, cursor):
    # Fetch all recipes from the database and list them to the user
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    print("Available Recipes:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    # Prompt user to select a recipe to update
    recipe_id = int(input("Enter the ID of the recipe you want to update: "))

    # Prompt user to select the column to update
    print("Columns available for update: name, cooking_time, ingredients")
    column = input("Enter the column to be updated: ")

    # Prompt user for the new value
    new_value = input("Enter the new value: ")

    # Prepare and execute SQL query to update the specified column
    if column == 'cooking_time' or column == 'ingredients':
        # Recalculate the difficulty if cooking_time or ingredients are updated
        cursor.execute("SELECT cooking_time, ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        old_cooking_time, old_ingredients = cursor.fetchone()

        # Update the specified column and recalculate difficulty
        query = f"UPDATE Recipes SET {column} = %s, difficulty = %s WHERE id = %s"
        if column == 'cooking_time':
            difficulty = calculate_difficulty(int(new_value), old_ingredients.split(", "))
        else:
            difficulty = calculate_difficulty(old_cooking_time, new_value.split(", "))
        cursor.execute(query, (new_value, difficulty, recipe_id))
    else:
        # Update the specified column
        query = f"UPDATE Recipes SET {column} = %s WHERE id = %s"
        cursor.execute(query, (new_value, recipe_id))

    # Commit the changes
    conn.commit()
    print("Recipe updated successfully!")

# Define delete_recipe function
def delete_recipe(conn, cursor):
    # Fetch all recipes from the database and list them to the user
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()
    print("Available Recipes:")
    for recipe in recipes:
        print(f"{recipe[0]}. {recipe[1]}")

    # Prompt user to select a recipe for deletion
    recipe_id = int(input("Enter the ID of the recipe you want to delete: "))

    # Prepare and execute SQL query to delete the specified recipe
    query = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(query, (recipe_id,))

    # Commit the changes
    conn.commit()
    print("Recipe deleted successfully!")


# Define main_menu function
def main_menu(conn, cursor):
    while True:
        print("\nMain Menu:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

    # Commit changes and close connection before exiting
    conn.commit()
    conn.close()
    print("Database connection closed.")

# Call the main_menu function
main_menu(conn, cursor)