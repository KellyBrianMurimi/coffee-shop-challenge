class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        print(f"[Customer Created] Name: {self._name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        unique_coffees = list(set(order.coffee for order in self._orders))
        print(f"[Customer.coffees()] {self._name} has ordered {len(unique_coffees)} unique coffees.")
        return unique_coffees

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        print(f"[Order] {self._name} ordered {coffee.name} for ${price:.2f}")
        return order
