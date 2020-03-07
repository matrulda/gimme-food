from click.testing import CliRunner
from gimme_food.parse_recipe import ParseRecipe
from gimme_food.configure import read_config
import json
import pytest

@pytest.fixture
def ica_test_response():
    with open("tests/test_data/ica_test.json") as json_file:
        return json.load(json_file)

@pytest.fixture
def conf():
    return read_config(None)

def no_responses():
    for response in ["no", "Röda linser", "Ingefära", "Grönsaksbuljong"]:
        yield response

def test_convert_to_gimme_food_dict_yes(ica_test_response, conf, mocker):
    mocker.patch('gimme_food.parse_recipe.input', return_value="y")
    recipe_parser = ParseRecipe(conf)
    result = recipe_parser.convert_to_gimme_food_dict(ica_test_response)
    assert len(result["ingredients"]) == 18
    assert "Ris" in result["ingredients"]

def test_convert_to_gimme_food_dict_no(ica_test_response, conf, mocker):
    mocker.patch('gimme_food.parse_recipe.input', side_effect=no_responses())
    recipe_parser = ParseRecipe(conf)
    result = recipe_parser.convert_to_gimme_food_dict(ica_test_response)
    assert len(result["ingredients"]) == 18
    assert "Port ris" in result["ingredients"]
    assert "Ingefära" in result["ingredients"]
