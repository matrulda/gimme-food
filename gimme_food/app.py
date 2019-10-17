import click
from gimme_food import __version__
import random
from gimme_food.recipe_db import *
import yaml

@click.command("gimme_food")
@click.option("--config", "-c", default="gimme_food/config/config.yaml",
                                help="Path to config file")
@click.option('--number-of-recipes','-n', default=1, help='Number of recipes')
@click.version_option(__version__)

def run_app(number_of_recipes, config):
    conf = read_config(config)
    recipe_list = make_recipe_db(conf["recipe_folder"])
    chosen_recipes = get_random_recipes(recipe_list, number_of_recipes)
    for recipe in chosen_recipes:
        r = recipe["recipe"]
        click.echo("This is a nice recipe: {}".format(r["name"]))
        click.echo("Shopping list:")
        for k, v in r["ingredients"].items():
            click.echo("{} {} {}".format(v["amount"], v["amount_type"], k))

def get_random_recipes(recipe_list, number_of_recipes):
    return random.sample(recipe_list, number_of_recipes)

def read_config(config):
    with open(config) as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    run_app()
