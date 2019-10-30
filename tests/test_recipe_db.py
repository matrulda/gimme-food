import pytest
import json
from json.decoder import JSONDecodeError
from gimme_food.exceptions import RecipeNotInProperJsonFormat
from gimme_food.recipe_db import read_recipe

@pytest.fixture
def file_path():
    return "gimme_food/examples/recipe_1.json"

def test_json_error(file_path, mocker):
    mocker.patch('json.load', side_effect=JSONDecodeError("", "", 0))
    with pytest.raises(RecipeNotInProperJsonFormat):
        read_recipe(file_path)
