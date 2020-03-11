import pytest
import json
from gimme_food.recipe_db import make_recipe_db
from gimme_food.recipe_picker import RecipePicker

@pytest.fixture
def recipe_list():
    return make_recipe_db("gimme_food/examples", 1)

def test_one_ingredient(recipe_list):
    recipe_picker = RecipePicker(recipe_list, 1, ("Jordnötssmör",))
    chosen_recipes = recipe_picker.get_recipes()
    assert len(chosen_recipes) == 1
    assert chosen_recipes[0].name == "Fruktig kokosmjölksgryta"

def test_two_ingredient(recipe_list):
    recipe_picker = RecipePicker(recipe_list, 1, ("Jordnötssmör","Gul lök"))
    chosen_recipes = recipe_picker.get_recipes()
    assert len(chosen_recipes) == 1
    assert chosen_recipes[0].name == "Fruktig kokosmjölksgryta"

def test_one_ingredient_two_recipes(recipe_list):
    recipe_picker = RecipePicker(recipe_list, 2, ("Jordnötssmör",))
    chosen_recipes = recipe_picker.get_recipes()
    assert len(chosen_recipes) == 2
