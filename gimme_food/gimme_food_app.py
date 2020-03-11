import click
import logging
import sys

from gimme_food import __version__
from gimme_food.recipe_db import make_recipe_db
from gimme_food.utils import present_result, print_banner
from gimme_food.configure import read_config, get_logger
from gimme_food.exceptions import RecipeNotInProperJsonFormat
from gimme_food.exceptions import NotEnoughRecipesInDatabase
from gimme_food.recipe_picker import RecipePicker

@click.command("gimme_food")
@click.option("--config", "-c", default=None, help="Path to config file", type=click.Path())
@click.option('--number-of-recipes','-n', default=1, help='Number of recipes')
@click.option('--ingredient', '-i', help="Ingredient to include", multiple=True)
@click.option('--debug/--no-debug','-d', default=False, help='Set log level to DEBUG')
@click.version_option(__version__)

def run_app(number_of_recipes, config, ingredient, debug):
    conf = read_config(config)
    log = get_logger(debug, conf["log_file"])
    print_banner(__version__)
    print_safe_config = {k:v for k,v in conf.items() if k != "secret"}
    log.info(f"gimme-food started - version: {__version__}, config: {print_safe_config}, " +
             f"number of recipes: {number_of_recipes}, ingredient: {ingredient}, debug: {debug}")
    try:
        recipe_list = make_recipe_db(conf["recipe_folder"], number_of_recipes)
    except (RecipeNotInProperJsonFormat, NotEnoughRecipesInDatabase) as e:
        log.error(e)
        sys.exit()
    recipe_picker = RecipePicker(recipe_list, number_of_recipes, ingredient)
    chosen_recipes = recipe_picker.get_recipes()
    present_result(chosen_recipes)
    log.info("gimme-food complete")

if __name__ == '__main__':
    run_app()
