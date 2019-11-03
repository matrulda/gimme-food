# Gimme food
[![Build Status](https://travis-ci.com/matrulda/gimme-food.svg?branch=master)](https://travis-ci.com/matrulda/gimme-food)
[![codecov](https://codecov.io/gh/matrulda/gimme-food/branch/master/graph/badge.svg)](https://codecov.io/gh/matrulda/gimme-food)


A simple application for getting saved recipes and a shopping list for making the yummy food.
The main idea is to be able to save your favorite recipes and to easily make a shopping list when it's time for the weekly shopping or "storhandling" as we say in Swedish.  
**Note: This repo is under heavy development!**

## Installation
```
git clone git@github.com:matrulda/gimme-food.git
cd gimme-food
pip install -r requirements/prod .
```
## Recipe "database"
The recipe database is a folder with json files, with one recipe in each.
Specify this folder in the config, see `config/config.yaml`. For data structure
of recipes, see `gimme_food/examples`.
**Note: This will most likely be replaced with a proper database later in development.
The json recipes might stick around for adding the recipes to the database though.**

## Usage
```
$ gimme_food -n 2
The following recipes were chosen:
Linscurry med kokosmjölk och lime: https://www.ica.se/recept/linscurry-med-kokosmjolk-och-lime-720274/
Fruktig kokosmjölksgryta: https://undertian.com/recept/fruktig-kokosmjolksgryta/

Here's your shopping list:
4 portion Ris
0.2 liter Torkade röda linser
3 piece Gul lök
0.01 liter Färsk ingefära
0.01 liter Sambal oelek
0.01 liter Olja
4 piece Vitlöksklyfta
0.04 liter Curry
0.01 liter Tomatpuré
0.5 liter Grönsaksbuljong
1.2 liter Kokosmjölk
0.5 piece Blomkålshuvud
250 gram Körsbärstomater
1 piece Lime
Salt
Peppar
65 gram Babyspenat
0.1 liter Cashewnötter
1 liter Kokade kikärtor
0.05 liter Jordnötssmör
400 gram Krossade tomater
3 piece Banan
225 gram Frusen mango
1 piece Grönsaksbuljongtärning

```

## Note regarding measures
Since this is an app to help me in my everyday life and I mainly use Swedish recipes, Swedish measures will be used. In later versions different language options might be possible.
