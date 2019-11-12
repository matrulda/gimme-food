import click
import random
import logging
import sys

from gimme_food import __version__
from gimme_food.recipe_db import make_recipe_db
from gimme_food.utils import present_result, print_banner
from gimme_food.configure import read_config, get_logger
from gimme_food.exceptions import RecipeNotInProperJsonFormat

@click.command("gimme_food")
@click.option("--config", "-c", default=None, help="Path to config file", type=click.Path())
@click.option('--number-of-recipes','-n', default=1, help='Number of recipes')
@click.option('--debug/--no-debug','-d', default=False, help='Set log level to DEBUG')
@click.version_option(__version__)

def run_app(number_of_recipes, config, debug):
    conf = read_config(config)
    log = get_logger(debug, conf["log_file"])
    print_banner(__version__)
    log.info(f"gimme-food started - version: {__version__}, config: {config}, " +
             f"number of recipes: {number_of_recipes}, debug: {debug}")
    log.info(f"config values: {conf}")
    try:
        recipe_list = list(make_recipe_db(conf["recipe_folder"]))
    except RecipeNotInProperJsonFormat as e:
        log.error(e)
        sys.exit()

    chosen_recipes = get_random_recipes(recipe_list, number_of_recipes)
    present_result(chosen_recipes)
    log.info("gimme-food complete")

def get_random_recipes(recipe_list, number_of_recipes):
    return random.sample(recipe_list, number_of_recipes)

if __name__ == '__main__':
    run_app()
