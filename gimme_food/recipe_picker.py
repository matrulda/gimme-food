import random
import logging

log = logging.getLogger("master")

class RecipePicker():

    def __init__(self, recipe_list, number_of_recipes, ingredient):
        self.recipe_list = recipe_list
        self.number_of_recipes = number_of_recipes
        self.ingredient = ingredient

    def get_overlaps(self, recipes, wanted_ingredients):
        log.debug("Getting overlap")
        overlaps = {}
        for recipe in recipes:
            overlap = set(recipe.ingredients_as_str()).intersection(wanted_ingredients)
            overlaps[recipe] = overlap
        log.debug(f"Overlaps dict: {overlaps}")
        return overlaps

    def find_recipes(self, recipes):
        chosen_recipes = []
        wanted_ingredients = list(self.ingredient)
        while len(wanted_ingredients) > 0:
            if len(chosen_recipes) == self.number_of_recipes:
                log.warning(f"Was not able to find all wanted ingredients in " +
                            "the desired number of recipes. Providing the best match found.")
                log.warning("The following wanted ingredients are not included in chosen recipes: " +
                            f"{wanted_ingredients}\n")
                break
            overlaps = self.get_overlaps(recipes, wanted_ingredients)
            max_key, max_value = max(overlaps.items(), key = lambda x: len(x[1]))
            log.debug(f"Recipe {max_key} had max overlap with {max_value}")
            if len(max_value) > 0:
                chosen_recipes.append(max_key)
                recipes.remove(max_key)
                for found_ingredient in overlaps[max_key]:
                    wanted_ingredients.remove(found_ingredient)
            else:
                log.warning(f"The following ingredients couldn't be found: {wanted_ingredients}")
                break
        return(chosen_recipes)

    def get_recipes(self):
        if len(self.ingredient) == 0:
            log.debug("No ingredients specified, returning random recipes")
            return self.get_random_recipes(self.recipe_list, self.number_of_recipes)
        else:
            shuffled_list = self.recipe_list
            random.shuffle(shuffled_list)
            log.debug(f"Shuffled recipe list: {shuffled_list}")
            chosen_recipes = self.find_recipes(shuffled_list)
            if len(chosen_recipes) < self.number_of_recipes:
                log.debug("Ingredients found in less than the desired number of recipes")
                recipes_not_chosen = [recipe for recipe in shuffled_list if recipe not in chosen_recipes]
                log.debug(f"Will add random recipes from {recipes_not_chosen}")
                for recipe in self.get_random_recipes(recipes_not_chosen, self.number_of_recipes - len(chosen_recipes)):
                    chosen_recipes.append(recipe)
            log.debug(f"Chosen recipes: {chosen_recipes}")
            return chosen_recipes


    def get_random_recipes(self, recipe_list, number_of_recipes):
        return random.sample(recipe_list, number_of_recipes)
