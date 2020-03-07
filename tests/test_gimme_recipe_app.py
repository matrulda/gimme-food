from click.testing import CliRunner
from gimme_food.gimme_recipe_app import run_app
import json
import pytest
import requests


class mock_response(object):

    def  __init__(self, ok=True):
        self.ok = ok

    def json(self):
        with open("tests/test_data/ica_test.json") as json_file:
            return json.load(json_file)

    def ok(self):
        return self.ok


def test_run_app(mocker):
    mocker.patch('gimme_food.parse_recipe.requests.get', return_value=mock_response())
    mocker.patch('gimme_food.parse_recipe.input', return_value="y")
    mocker.patch('gimme_food.parse_recipe.open')
    mocker.patch('gimme_food.parse_recipe.json.dump')
    runner = CliRunner()
    result = runner.invoke(run_app, ['-u www.ica.se/recept/god-mat-1233/'])
    assert result.exit_code == 0

def test_run_app_not_implemented(mocker):
    mocker.patch('gimme_food.parse_recipe.requests.get', return_value=mock_response())
    mocker.patch('gimme_food.parse_recipe.input', return_value="y")
    mocker.patch('gimme_food.parse_recipe.open')
    mocker.patch('gimme_food.parse_recipe.json.dump')
    runner = CliRunner()
    result = runner.invoke(run_app, ['-u www.tasty.com/recept/yum-yum/'])
    assert result.exit_code == 1

def test_run_app_connection_error(mocker):
    mocker.patch('gimme_food.parse_recipe.requests.get', return_value=mock_response(ok=False))
    mocker.patch('gimme_food.parse_recipe.input', return_value="y")
    mocker.patch('gimme_food.parse_recipe.open')
    mocker.patch('gimme_food.parse_recipe.json.dump')
    runner = CliRunner()
    result = runner.invoke(run_app, ['-u www.ica.se/recept/god-mat-1233/'])
    assert result.exit_code == 1
