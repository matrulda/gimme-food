from click.testing import CliRunner
from gimme_food.app import run_app

def test_run_app():
    runner = CliRunner()
    result = runner.invoke(run_app, ['-n 1'])
    assert result.exit_code == 0

def test_run_app_two_recipes():
    runner = CliRunner()
    result = runner.invoke(run_app, ['-n 2'])
    assert result.exit_code == 0

def test_run_app_with_ingredient():
    runner = CliRunner()
    result = runner.invoke(run_app, ['-n 1', '-i "Gul lök"'])
    assert result.exit_code == 0
