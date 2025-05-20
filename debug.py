from customer import Customer
from coffee import Coffee
from order import Order


C1 = Customer("Jane")
C2 = Customer("John")

# C3 = Customer("Supercalifragalistic")
# C4 = Customer("")


Co1 = Coffee("Latte")
Co2 = Coffee("Maciatto")

# Co3 = Coffee("Oh")

Co4 = Coffee("Espresso")
Co5 = Coffee("Americano")
Co6 = Coffee("Depresso")


# Tests for Customer name validation
O1 = Order(C1, Co2, 8.50)
O2 = Order(C2, Co1, 6.40)

# O3 = Order(C3, Co1, 8.50)
# O4 = Order(C4, Co2, 8.50)


# Tests for Coffee name validation
# O5 = Order(C1, Co3, 8.50)
# O6 = Order(C2, Co3, 8.50)


# Tests for Order price validation
# O7 = Order(C1, Co2, 0.50)
# O8 = Order(C2, Co2, 18.50)


# Tests for Unique Coffee orders
O9 = Order(C1, Co4, 7.60)
O4 = Order(C1, Co2, 8.50)
O5 = Order(C1, Co5, 5.50)


# Tests for Unique Customer orders
O6 = Order(C2, Co4, 7.60)
O7 = Order(C2, Co2, 8.50)
O8 = Order(C2, Co5, 5.50)
O9 = Order(C1, Co5, 3.50)
O10 = Order(C2, Co1, 6.50)
O11 = Order(C2, Co5, 5.50)


#Test for create_order association
C1.create_order(Co4, 8.50)
C2.create_order(Co5, 4.50)


print([O.coffee.name for O in C1.orders()])
print([O.coffee.name for O in C2.orders()])
# print([O.coffee.name for O in C3.orders()])
# print([O.coffee.name for O in C4.orders()])


# Tests for unique_coffee list
print("Jane's Coffees:", [coffee.name for coffee in C1.unique_coffees()])
print("John's Coffees:", [coffee.name for coffee in C2.unique_coffees()])


# Tests for unique_customer list
print("Latte Customers:", [customer.name for customer in Co1.unique_customers()])
print("Maciatto Customers:", [customer.name for customer in Co2.unique_customers()])
print("Espresso Customers:", [customer.name for customer in Co4.unique_customers()])
print("Americano Customers:", [customer.name for customer in Co5.unique_customers()])


#Test for all_orders after create_order
print("All Orders:")
for order in Order.all():
    print(f"{order.customer.name} ordered {order.coffee.name} at ${order.price}")


#Test for order number aggregation
print("Number of Latte orders: ", Co1.num_orders())
print("Number of Maciatto orders: ", Co2.num_orders())
print("Number of Espresso orders: ", Co4.num_orders())
print("Number of Americano orders: ", Co5.num_orders())
print("Number of Depresso orders: ", Co6.num_orders())


#Test for average_price aggregation
print("Average Latte Price:", Co1.average_price())
print("Average Maciatto Price:", Co2.average_price())
print("Average Espresso Price:", Co4.average_price())
print("Average Americano Price:", Co5.average_price())
print("Average Depresso Price:", Co6.average_price())


#Test for most_aficionado
print("Latte aficionado: ", Customer.most_aficionado(Co1).name if Customer.most_aficionado(Co1) else "None")
print("Maciatto aficionado: ", Customer.most_aficionado(Co2).name if Customer.most_aficionado(Co2) else "None")
print("Espresso aficionado: ", Customer.most_aficionado(Co4).name if Customer.most_aficionado(Co4) else "None")
print("Americano aficionado: ", Customer.most_aficionado(Co5).name if Customer.most_aficionado(Co5) else "None")
print("Depresso aficionado: ", Customer.most_aficionado(Co6).name if Customer.most_aficionado(Co6) else "None")