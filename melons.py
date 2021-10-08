from random import randrange
from datetime import datetime, date, time
"""Classes for melon orders."""
class AbstractMelonOrder():
        def get_base_price(self):
            base_price = randrange(5,10)
            print(base_price)
            
            if datetime.now() > datetime.time(8,0,0) or datetime.now() < datetime.time(12,0,0):
                base_price = base_price + 4
                print(base_price)

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

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
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
 