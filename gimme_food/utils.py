from collections import defaultdict
import os
import yaml

from gimme_food.entities.amount import Amount

def present_result(chosen_recipes):
    shopping_dict = sum_ingredients(chosen_recipes)
    print("The following recipes were chosen:")
    for recipe in chosen_recipes:
        print(recipe)
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
            shopping_dict[ingredient.name] = a.sum(shopping_dict[ingredient.name])
    return shopping_dict

def read_config(config):
    default_config = False
    if config is None:
        default_config = True
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config = os.path.join(script_dir, "config", "config.yaml")
    with open(config) as f:
        config_dict = yaml.safe_load(f)
    if default_config:
        for key in config_dict:
            config_dict[key] = os.path.join(os.path.dirname(script_dir), config_dict[key])
    return config_dict
