class Coffee:

    def __init__(self, name):
        if type(name) != str or len(name) < 3:
            raise ValueError("Name must be string of at least 3 characters.")
        
        self._name = name


    @property
    def name(self):
        return self._name
    

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]


    def unique_customers(self):
        orders = self.orders()
        unique_customers = []

        for order in orders:
            if order.customer not in unique_customers:
                unique_customers.append(order.customer)
        
        return unique_customers
    

    def num_orders(self):
        return len(self.orders())
    
    
    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            avg =  total / len(orders)
            return round(avg, 2)
        return 0
        