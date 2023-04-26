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
def ica_test_response_2():
    with open("tests/test_data/ica_test_long_rice_name.json") as json_file:
        return json.load(json_file)

@pytest.fixture
def conf():
    return read_config(None)

# Do not convert to portions of rice
def responses_1():
    for response in ["no", "Röda linser", "Ingefära", "Grönsaksbuljong"]:
        yield response

# Change name of rice and then convert to portions of rice 
def responses_2():
    for response in ["Ris", "yes", "Röda linser", "Ingefära", "Grönsaksbuljong"]:
        yield response

def test_convert_to_gimme_food_dict_yes(ica_test_response, conf, mocker):
    mocker.patch('gimme_food.parse_recipe.input', return_value="y")
    recipe_parser = ParseRecipe(conf)
    result = recipe_parser.convert_to_gimme_food_dict(ica_test_response)
    assert len(result["ingredients"]) == 18
    assert "Ris" in result["ingredients"]

def test_convert_to_gimme_food_dict_no(ica_test_response, conf, mocker):
    mocker.patch('gimme_food.parse_recipe.input', side_effect=responses_1())
    recipe_parser = ParseRecipe(conf)
    result = recipe_parser.convert_to_gimme_food_dict(ica_test_response)
    assert len(result["ingredients"]) == 18
    assert "Port ris" in result["ingredients"]
    assert "Ingefära" in result["ingredients"]

def test_convert_to_gimme_food_dict_change_name_and_convert_to_portion(
        ica_test_response_2, conf, mocker):
    mocker.patch('gimme_food.parse_recipe.input', side_effect=responses_2())
    recipe_parser = ParseRecipe(conf)
    result = recipe_parser.convert_to_gimme_food_dict(ica_test_response_2)
    assert len(result["ingredients"]) == 18
    assert "Ris" in result["ingredients"]
    assert "Ingefära" in result["ingredients"]

def test_get_recipe_file_name():
    recipe_name = "Potatis, morot och palsternacka"
    result = ParseRecipe.get_recipe_file_name(recipe_name)
    assert result == "potatis_morot_och_palsternacka.json"

