import json
from json.decoder import JSONDecodeError
import os
from gimme_food.entities.recipe import Recipe
from gimme_food.exceptions import RecipeNotInProperJsonFormat

def read_recipe(file_path):
    with open(file_path) as json_file:
        try:
            return json.load(json_file)
        except JSONDecodeError:
            raise RecipeNotInProperJsonFormat("Oops, it looks like your recipe, " +
                                              f"{file_path}, isn't a valid json file. " +
                                              "Try running it in a json validator.")

def make_recipe_db(recipe_folder):
    for file in os.listdir(recipe_folder):
        if file.endswith(".json"):
            recipe_dict = read_recipe(os.path.join(recipe_folder, file))
            yield Recipe(recipe_dict)
