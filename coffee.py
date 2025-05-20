class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._orders = []
        print(f"[Coffee Created] Name: {self._name}")

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        print(f"[Coffee.num_orders()] {self._name} has {len(self._orders)} orders.")
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        average = sum(order.price for order in self._orders) / len(self._orders)
        return average
