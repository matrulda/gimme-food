import click
import random

from gimme_food import __version__
from gimme_food.recipe_db import make_recipe_db
from gimme_food.utils import present_result, read_config

@click.command("gimme_food")
@click.option("--config", "-c", default=None, help="Path to config file")
@click.option('--number-of-recipes','-n', default=1, help='Number of recipes')
@click.version_option(__version__)

def run_app(number_of_recipes, config):
    conf = read_config(config)
    recipe_list = list(make_recipe_db(conf["recipe_folder"]))
    chosen_recipes = get_random_recipes(recipe_list, number_of_recipes)
    present_result(chosen_recipes)

def get_random_recipes(recipe_list, number_of_recipes):
    return random.sample(recipe_list, number_of_recipes)

if __name__ == '__main__':
    run_app()
