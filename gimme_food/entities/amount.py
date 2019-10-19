class Amount(object):
    """
    Object that represent an amount
    """

    def __init__(self, quantity, amount_type):
        self.quantity = quantity
        self.amount_type = amount_type

    def __str__(self):
        if self.quantity == "unknown":
            quantity = self.quantity
        else:
            quantity = round(self.quantity, 2)
        return "{} {}".format(quantity, self.amount_type)

    def __repr__(self):
        return self.__str__()

    def sum(self, other):
        """
        Returns an amount that is the sum of this amount object and another
        if comp is empty dict, return self
        :param comp: Amount object or empty dict return self
        :raises IncompatibleAmountTypes
        """
        if isinstance(other, dict):
            return self
        elif self.quantity == "unknown":
            return other
        elif other.quantity == "unknown":
            return self
        elif self.amount_type == other.amount_type:
            return Amount(self.quantity + other.quantity, self.amount_type)
        else:
            raise IncompatibleAmountTypes(
                  "Unable to sum the following amounts: \n - {} \n - {}".format(self, other))


class IncompatibleAmountTypes(Exception):
    pass
