class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str or not (1 <= len(name) <= 15):
            raise ValueError("Name must be string between 1 and 15 characters.")
        
        self._name = name

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]
    

    def unique_coffees(self):
        orders = self.orders()
        unique_coffees = []

        for order in orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        
        return unique_coffees