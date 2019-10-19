from gimme_food.entities.amount import Amount

class Ingredient(object):
    """
    Object that represent an Ingredient
    """

    def __init__(self, name, amount_object):
        self.name = name
        self.amount = amount_object

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
        
