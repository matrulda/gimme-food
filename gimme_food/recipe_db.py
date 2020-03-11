import json
from json.decoder import JSONDecodeError
import os
from gimme_food.entities.recipe import Recipe
from gimme_food.exceptions import RecipeNotInProperJsonFormat
from gimme_food.exceptions import NotEnoughRecipesInDatabase
import logging

log = logging.getLogger("master")

def read_recipe(file_path):
    with open(file_path) as json_file:
        try:
            return json.load(json_file)
        except JSONDecodeError:
            raise RecipeNotInProperJsonFormat("Oops, it looks like your recipe, " +
                                              f"{file_path}, isn't a valid json file. " +
                                              "Try running it in a json validator.")

def make_recipe_db(recipe_folder, number_of_recipes):
    recipe_list = []
    for f in os.listdir(recipe_folder):
        if f.endswith(".json"):
            log.debug(f"Reading recipe file: {f}")
            recipe_dict = read_recipe(os.path.join(recipe_folder, f))
            recipe_list.append(Recipe(recipe_dict))
    if len(recipe_list) < number_of_recipes:
        raise NotEnoughRecipesInDatabase(f"You asked for {number_of_recipes} recipes " +
                                         f"but there is only {len(recipe_list)} in your database, " +
                                         "add more recipes or try a lower number of recipes")
    else:
        return recipe_list
