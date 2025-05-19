from customer import Customer
from coffee import Coffee

class Order:

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee

        if type(price) == float and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Order price can only be between $1.00 and $10.00")
    
    @property
    def customer(self):
        return self._customer
    
    @property 
    def coffee(self):
        return self._coffee
    
    @property 
    def price(self):
        return self._price