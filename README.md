# Gimme food
A simple application for getting saved recipes and a shopping list for making the yummy food.
The main idea is to be able to save your favorite recipes and to easily make a shopping list when it's time for the weekly shopping or "storhandling" as we say in Swedish.  
**Note: This repo is under heavy development!**

## Installation
```
git clone git@github.com:MatildaAslin/gimme-food.git
cd gimme-food
pip install .
```
## Recipe "database"
The recipe database is a folder with json files, with one recipe in each.
Specify this folder in the config, see `config/config.yaml`. For data structure
of recipes, see `tests/resources`.
**Note: This will most likely be replaced with a proper database later in development.
The json recipes might stick around for adding the recipes to the database though.**

## Usage
```
gimme_food --config my_config.yaml --number-of-recipes 2
```

## Note regarding measures
Since this is an app to help me in my everyday life and I mainly use Swedish recipes, Swedish measures will be used. In later versions different language options might be possible.
