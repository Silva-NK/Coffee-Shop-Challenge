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
O3 = Order(C1, Co4, 7.60)
O4 = Order(C1, Co2, 8.50)
O5 = Order(C1, Co5, 5.50)


# Tests for Unique Customer orders
O6 = Order(C2, Co4, 7.60)
O7 = Order(C2, Co2, 8.50)
O8 = Order(C2, Co5, 5.50)
O9 = Order(C1, Co5, 3.50)
O10 = Order(C2, Co1, 6.50)
O11 = Order(C2, Co5, 5.50)

print([O.coffee.name for O in C1.orders()])
print([O.coffee.name for O in C2.orders()])
# print([O.coffee.name for O in C3.orders()])
# print([O.coffee.name for O in C4.orders()])

# Tests for unique_coffee list
print("C1's Coffees:", [coffee.name for coffee in C1.unique_coffees()])
print("C2's Coffees:", [coffee.name for coffee in C2.unique_coffees()])

# Tests for unique_customer list
print("Co1's Coffees:", [customer.name for customer in Co1.unique_customers()])
print("Co2's Coffees:", [customer.name for customer in Co2.unique_customers()])
print("Co4's Coffees:", [customer.name for customer in Co4.unique_customers()])
print("Co5's Coffees:", [customer.name for customer in Co5.unique_customers()])