#!/usr/bin/env python

from setuptools import setup, find_packages
from gimme_food import __version__

setup(name='gimme_food',
      version=__version__,
      description='App for getting recipes and a shopping list',
      author='Matilda Åslin',
      author_email='matilda@åslin.se',
      python_requires='>=3',
      packages=find_packages(exclude=["tests"]),
      entry_points={
        'console_scripts': 'gimme_food = gimme_food.app:run_app'}
     )
