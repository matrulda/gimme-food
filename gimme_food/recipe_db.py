import json
import os

def read_recipe(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

def make_recipe_db(recipe_folder):
    recipes = []
    for file in os.listdir(recipe_folder):
        if file.endswith(".json"):
            recipe = read_recipe(os.path.join(recipe_folder, file))
            recipes.append(recipe)
    return recipes
