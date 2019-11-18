from gimme_food.entities.ingredient import Ingredient
from gimme_food.entities.amount import Amount

class Recipe(object):
    """
    Object that represents a recipe
    """

    def __init__(self, recipe_dict):
        r = recipe_dict["recipe"]
        self.name = r["name"]
        self.url = r["url"]
        self.portions = r["portions"]
        self.ingredients = list(self.make_ingredients(r["ingredients"]))

    def __str__(self):
        return "{}: {}".format(self.name, self.url)

    def __repr__(self):
        return self.__str__()

    def make_ingredients(self, ingredients):
        for name, amount_info in ingredients.items():
            yield Ingredient(name, Amount.create_amount_subclass(amount_info["amount"],
                                                                 amount_info["amount_type"]))

    def ingredients_as_str(self):
        for ingredient in self.ingredients:
            yield ingredient.name
