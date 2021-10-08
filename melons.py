from random import randrange
from datetime import datetime, date, time
"""Classes for melon orders."""
class AbstractMelonOrder():
        def get_base_price(self):
            base_price = randrange(5,10)
            print(base_price)
            today = datetime.now()
            if (today.hour > 8 and today.hour < 11) and (date.isoweekday(today) != 6 or date.isoweekday(today) != 7):
                base_price = base_price + 4
            return base_price

           
        def get_total(self):
            """Calculate price, including tax."""

            base_price = self.get_base_price()
            if self.species == 'Christmas melons':
                base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * base_price

            return total

        def mark_shipped(self):
            """Record the fact than an order has been shipped."""

            self.shipped = True

class TooManyMelonsError(ValueError):
    pass
    # def __init__(self, expression, message):
    #     self.expression = self.qty > 100
    #     self.message = "No more than 100 melons!"
    
    #def too_many(self):
        # if self.qty > 100:
        #     print(self.message)

class DomesticMelonOrder(AbstractMelonOrder, TooManyMelonsError):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08
        
        if self.qty >100:
            raise TooManyMelonsError
        else:
            self.qty = qty

class InternationalMelonOrder(AbstractMelonOrder, TooManyMelonsError):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.qty < 10:
            base_price = base_price + 3
        total = (1 + self.tax) * self.qty * base_price

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    passed_inspection = False

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
        else:
            self.passed_inspection = False

        