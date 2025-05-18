from customer import Customer
from coffee import Coffee

kelly = Customer("Kelly")
beth = Customer("Beth")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

order1 = kelly.create_order(latte, 4.5)
order2 = kelly.create_order(mocha, 5.0)
order3 = beth.create_order(latte, 6.0)

print(f"{kelly.name} ordered {[c.name for c in kelly.coffees()]}")
print(f"Total orders for Latte: {latte.num_orders()}")
print(f"Average price of Latte: {latte.average_price():.2f}")
