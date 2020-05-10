import requests
import os
import json
import logging
from collections import defaultdict

log = logging.getLogger("master")

class ParseRecipe(object):

    def __init__(self, conf):
        self.conf = conf

    def parse_recipe(self, url):
        if "www.ica.se" in url:
            recipe = self.get_ica_recipe(url)
            recipe_file_name = ParseRecipe.get_recipe_file_name(recipe["recipe"]["name"])
            file_name = os.path.join(self.conf["recipe_folder"], recipe_file_name)
            print(f"\nRecipe captured! Writing to: {file_name}")
            with open(file_name, "w") as f:
                json.dump(recipe, f, indent=4, ensure_ascii=False)
        else:
            raise NotImplementedError("Sorry, only ICA recipes are supported for the moment")

    @staticmethod
    def get_recipe_file_name(recipe_name):
        recipe_name = recipe_name.lower()
        recipe_name = recipe_name.replace(" ", "_")
        recipe_name = recipe_name.replace(",", "")
        return f"{recipe_name}.json"

    def get_ica_recipe(self, url):
        try:
            ica_user = self.conf["secret"]["ica_user"]
            ica_pass = self.conf["secret"]["ica_pass"]
        except:
            raise Exception("Could not load ICA credentials from config")
        request_url = self.construct_ica_request_url(url)
        log.debug(f"Request url: {request_url}")
        response = requests.get(request_url, auth=(ica_user, ica_pass))
        if response.ok:
            with open("ica_test.json", "w") as f:
                json.dump(response.json(), f, indent=4)
            response_dict = self.convert_to_gimme_food_dict(response.json())
            # Add some final touches
            ica_recipe = {"recipe": response_dict}
            ica_recipe["recipe"]["url"] = url
            return ica_recipe
        else:
            raise Exception(f"Something went wrong, got {response}")

    def convert_to_gimme_food_dict(self, response_dict):
        gimme_food_dict = defaultdict()
        gimme_food_dict["name"] = response_dict["Title"]
        gimme_food_dict["portions"] = response_dict["IngredientGroups"][0]["Portions"]
        ingredients_dict = defaultdict()
        for i_group in response_dict["IngredientGroups"]:
            for i in i_group["Ingredients"]:
                i_name = i["Ingredient"].capitalize()
                i_name_words = i_name.split(" ")
                if i_name == "Salt och peppar":
                    ingredients_dict["Salt"] = {"amount": "unknown", "amount_type": "unknown"}
                    ingredients_dict["Peppar"] = {"amount": "unknown", "amount_type": "unknown"}
                    continue
                if len(i_name_words) > 2:
                    user_answer = input(f"\nIngredient name, {i_name}, is suspiciously long," +
                                        " perhaps it contains more than the ingredient name.\n" +
                                        "Do you want to use it? Type \"yes\". \n" +
                                        "Otherwise, type the name you want to use instead: ")
                    if user_answer.lower() != "yes" and user_answer.lower() != "y":
                        i_name = user_answer
                if "Port" in i_name_words[0]:
                    potential_i_name = " ".join(i_name_words[1:])
                    user_answer = input(f"\nShould, {i_name}, be interpreted as " +
                                     f"as portions of {potential_i_name}? (yes/no):\n")
                    if user_answer.lower() == "yes" or user_answer.lower() == "y":
                        ingredients_dict[potential_i_name.capitalize()] = {"amount": i["Quantity"], "amount_type": "portion"}
                    else:
                        ingredients_dict[i_name] = {"amount": i["Quantity"], "amount_type": "piece"}
                elif "Unit" in i:
                    ingredients_dict[i_name] = {"amount": i["Quantity"], "amount_type": i["Unit"]}
                elif i["Quantity"] == 0:
                    ingredients_dict[i_name] = {"amount": "unknown", "amount_type": "unknown"}
                else:
                    ingredients_dict[i_name] = {"amount": i["Quantity"], "amount_type": "piece"}
            gimme_food_dict["ingredients"] = ingredients_dict
        return gimme_food_dict

    def construct_ica_request_url(self, url):
        base_url = "https://handla.api.ica.se/api/recipes/recipe/"
        recipe_id = os.path.basename(url.strip("/")).split("-")[-1]
        return base_url + recipe_id
