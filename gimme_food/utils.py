from collections import defaultdict
import logging

from gimme_food.entities.amount import Amount
from gimme_food.entities.amount import IncompatibleAmountTypes
from gimme_food.exceptions import UnableToCalculateSumOfIngredient

log = logging.getLogger("master")

def present_result(chosen_recipes):
    log.debug(f"chosen recipes: {chosen_recipes}")
    shopping_dict = sum_ingredients(chosen_recipes)
    print("The following recipes were chosen:\n")
    for recipe in chosen_recipes:
        print(f"{recipe}\n")
    print("\nHere's your shopping list:")
    for name, amount in shopping_dict.items():
        if amount.quantity == "unknown":
            print(name)
        else:
            print("{} {}".format(amount, name))

def sum_ingredients(chosen_recipes):
    shopping_dict = defaultdict(dict)
    for recipe in chosen_recipes:
        for ingredient in recipe.ingredients:
            a = ingredient.amount
            log.debug(f"Attempting to sum: {a} and {shopping_dict[ingredient.name]}")
            try:
                shopping_dict[ingredient.name] = a.sum(shopping_dict[ingredient.name])
            except IncompatibleAmountTypes as e:
                raise UnableToCalculateSumOfIngredient(f"Unable to calculate sum for ingredient: \"{ingredient.name}\", " +
                                                       f"got the following error: {e}")
    return shopping_dict

def print_banner(version):
    banner = r"""
------------------------------------------------------------------
  ________.__                           _____                 .___
 /  _____/|__| _____   _____   ____   _/ ____\____   ____   __| _/
/   \  ___|  |/     \ /     \_/ __ \  \   __\/  _ \ /  _ \ / __ |
\    \_\  \  |  Y Y  \  Y Y  \  ___/   |  | (  <_> |  <_> ) /_/ |
 \______  /__|__|_|  /__|_|  /\___  >  |__|  \____/ \____/\____ |
        \/         \/      \/     \/                           \/
-------------------------------------------------------------------
                              v{}
                                                                   """.format(version)

    print(banner)
