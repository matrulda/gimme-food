import pytest
import json
from json.decoder import JSONDecodeError
from gimme_food.exceptions import RecipeNotInProperJsonFormat
from gimme_food.exceptions import NotEnoughRecipesInDatabase
from gimme_food.exceptions import InconsistentBD
from gimme_food.recipe_db import read_recipe
from gimme_food.recipe_db import make_recipe_db
from gimme_food.configure import read_config

@pytest.fixture
def file_path():
    return "gimme_food/examples/recipe_1.json"

@pytest.fixture
def conf():
    return read_config(None)

def test_json_error(file_path, mocker):
    mocker.patch('json.load', side_effect=JSONDecodeError("", "", 0))
    with pytest.raises(RecipeNotInProperJsonFormat):
        read_recipe(file_path)

def test_not_enough_recipes(conf):
    with pytest.raises(NotEnoughRecipesInDatabase):
        make_recipe_db(conf["recipe_folder"], 3)

def test_inconsistent_db():
    with pytest.raises(InconsistentBD):
        make_recipe_db("tests/test_data/test_inconsistent_db", 2)
