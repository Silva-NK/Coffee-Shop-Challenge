from customer import Customer
from coffee import Coffee

class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        
        self._customer = customer


        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        
        self._coffee = coffee


        if type(price) == float and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Order price can only be between $1.00 and $10.00")
      
        
        Order.all_orders.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @property 
    def coffee(self):
        return self._coffee
    
    @property 
    def price(self):
        return self._price
    
    @classmethod
    def all(cls):
        return cls.all_orders