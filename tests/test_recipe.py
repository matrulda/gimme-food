import pytest
import json
from gimme_food.entities.recipe import Recipe

@pytest.fixture
def recipe_dict():
    with open("gimme_food/examples/recipe_1.json") as json_file:
        return json.load(json_file)

def test_make_recipe(recipe_dict):
    recipe = Recipe(recipe_dict)
    assert str(recipe) == ("Linscurry med kokosmjölk och lime (4 portions): "
                           "https://www.ica.se/recept/linscurry-med-kokosmjolk-och-lime-720274/")
    assert len(list(recipe.ingredients)) == 18
