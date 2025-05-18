class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            print(f"Coffee created with name: {self._name}")
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        print(f"Fetching orders for coffee: {self._name}")
        return self._orders

    def customers(self):
        unique_customers = list(set(order.customer for order in self._orders))
        print(f"Unique customers who ordered {self._name}: {unique_customers}")
        return unique_customers

    def num_orders(self):
        print(f"Number of orders for {self._name}: {len(self._orders)}")
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            print(f"No orders for {self._name}. Average price is 0.")
            return 0
        avg_price = sum(order.price for order in self._orders) / len(self._orders)
        print(f"Average price for {self._name} is: {avg_price}")
        return avg_price
