

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
            for name in subclass.get_name_variants():
                if name == "unknown" and amount_type == "unknown":
                    return subclass(quantity)
                if amount_type == name[0]:
                    return subclass(quantity * name[1])
        raise AmountTypeUnknown(f"Unknown amount type: {amount_type}")

    @staticmethod
    def get_subclasses():
        return Amount.__subclasses__()

    def __str__(self):
        if self.quantity == "unknown":
            return f"{self.quantity} {self.get_name()}"
        else:
            return self.display_appropriate_size()

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_name():
        """
        Must be implemented by subclass
        """
        raise NotImplementedError

    @staticmethod
    def get_name_variants():
        """
        Must be implemented by subclass
        """
        raise NotImplementedError

    def display_appropriate_size(self):
        return f"{self.quantity} {self.get_name()}"

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

    @staticmethod
    def get_name_variants():
        name_list = [("liter", 1), ("dl", 0.1),
                     ("msk", 0.015), ("tsk", 0.005),
                     ("krm", 0.001), ("ml", 0.001)]
        return name_list

    def display_appropriate_size(self):
        quantity_ml = int(self.quantity * 1000)
        if quantity_ml < 1000:
            if quantity_ml % 100 == 0:
                return f"{round(self.quantity / 0.1)} dl"
            if quantity_ml % 100 == 50:
                if quantity_ml == 50:
                    return "1/2 dl"
                else:
                    return f"{round((self.quantity - 0.05) / 0.1)} 1/2 dl"
            elif quantity_ml % 15 == 0:
                return f"{round(self.quantity / 0.015)} msk"
            elif quantity_ml % 5 == 0 and quantity_ml <= 50:
                return f"{round(self.quantity / 0.005)} tsk"
            elif quantity_ml % 1 == 0:
                return f"{int(self.quantity / 0.001)} krm"
        return f"{round(self.quantity, 2)} liter"


class AmountPiece(Amount):

    @staticmethod
    def get_name():
        return "piece"

    @staticmethod
    def get_name_variants():
        return [("piece", 1)]

    def display_appropriate_size(self):
        if self.quantity % 1 == 0.5:
            if self.quantity == 0.5:
                return "1/2"
            else:
                return f"{round(self.quantity - 0.5)} 1/2"
        else:
            return f"{round(self.quantity)}"


class AmountGram(Amount):

    @staticmethod
    def get_name():
        return "gram"

    def get_name_variants():
        name_list = [("gram", 1), ( "g", 1),
                     ("kg", 1000)]
        return name_list

    def display_appropriate_size(self):
        if self.quantity >= 1000:
            return f"{round(self.quantity / 1000, 2)} kg"
        else:
            return f"{round(self.quantity)} gram"


class AmountUnknown(Amount):

    @staticmethod
    def get_name():
        return "unknown"

    @staticmethod
    def get_name_variants():
        return ["unknown"]

class AmountPortion(Amount):

    @staticmethod
    def get_name():
        return "portion"

    @staticmethod
    def get_name_variants():
        return [("portion", 1)]

    def display_appropriate_size(self):
        if self.quantity > 1:
            return f"{self.quantity} portioner"
        else:
            return f"{self.quantity} portion"


class IncompatibleAmountTypes(Exception):
    pass


class AmountTypeUnknown(Exception):
    pass
