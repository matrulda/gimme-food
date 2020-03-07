#!/usr/bin/env python

from setuptools import setup, find_namespace_packages
from gimme_food import __version__

setup(name='gimme_food',
      version=__version__,
      description='App for getting recipes and a shopping list',
      author='Matilda Åslin',
      author_email='matilda@åslin.se',
      python_requires='>=3',
      packages=find_namespace_packages(),
      package_data={'gimme_food': ['config/config.yaml', 'examples/recipe_1.json',
                                   'examples/recipe_2.json']},
      include_package_data=True,
      entry_points={
        'console_scripts': ['gimme_food = gimme_food.gimme_food_app:run_app',
                            'gimme_recipe = gimme_food.gimme_recipe_app:run_app']}
     )
