

class Amount(object):
    """
    Object that represent an amount
    """

    def __init__(self, quantity):
        self.quantity = quantity

    @staticmethod
    def create_amount_subclass(quantity, amount_type):
        subclasses = Amount.get_subclasses()
        for subclass in subclasses:
            if amount_type == subclass.get_name():
                return subclass(quantity)
        raise AmountTypeUnknown(f"Unknown amount type: {amount_type}")

    @staticmethod
    def get_subclasses():
        return Amount.__subclasses__()

    def __str__(self):
        if self.quantity == "unknown":
            quantity = self.quantity
        else:
            quantity = round(self.quantity, 2)
        return "{} {}".format(quantity, self.get_name())

    def __repr__(self):
        return self.__str__()

    def get_name():
        """
        Must be implemented by subclass
        """
        raise NotImplementedError

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
        elif type(self) is type(other):
            return Amount.create_amount_subclass(self.quantity + other.quantity, self.get_name())
        else:
            raise IncompatibleAmountTypes(
                  "Unable to sum the following amounts: \n - {} \n - {}".format(self, other))

class AmountLiter(Amount):

    @staticmethod
    def get_name():
        return "liter"


class AmountPiece(Amount):

    @staticmethod
    def get_name():
        return "piece"


class AmountGram(Amount):

    @staticmethod
    def get_name():
        return "gram"


class AmountUnknown(Amount):

    @staticmethod
    def get_name():
        return "unknown"


class AmountPortion(Amount):

    @staticmethod
    def get_name():
        return "portion"


class IncompatibleAmountTypes(Exception):
    pass

class AmountTypeUnknown(Exception):
    pass
