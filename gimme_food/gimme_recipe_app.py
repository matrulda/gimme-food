import click
import logging
import sys

from gimme_food import __version__
from gimme_food.configure import read_config, get_logger
from gimme_food.utils import print_banner
from gimme_food.parse_recipe import ParseRecipe

@click.command("gimme_recipe")
@click.option("--config", "-c", default=None, help="Path to config file", type=click.Path())
@click.option("--url", "-u", help="Recipe url to parse")
@click.option("--debug/--no-debug", "-d", default=False, help="Set log level to DEBUG")
@click.version_option(__version__)

def run_app(config, url, debug):
    conf = read_config(config)
    log = get_logger(debug, conf["log_file"])
    print_banner(__version__)
    print_safe_config = {k:v for k,v in conf.items() if k != "secret"}
    log.info(f"gimme-food started - version: {__version__}, " +
             f"config: {print_safe_config}, " +
             f"url: {url}, debug: {debug}")
    recipe_parser = ParseRecipe(conf)
    recipe_parser.parse_recipe(url)
    log.info("gimme-food complete")

if __name__ == '__main__':
    run_app()
