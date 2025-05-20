class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            print(f"[Coffee Created] Name: {self._name}")
        else:
            raise ValueError("Coffee name must be at least 3 characters long.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        customers_list = list(set(order.customer for order in self._orders))
        print(f"[Coffee.customers()] {self._name} has {len(customers_list)} unique customers.")
        return customers_list

    def num_orders(self):
        print(f"[Coffee.num_orders()] {self._name} has {len(self._orders)} orders.")
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            print(f"[Coffee.average_price()] No orders for {self._name}.")
            return 0
        avg = sum(order.price for order in self._orders) / len(self._orders)
        print(f"[Coffee.average_price()] Average price for {self._name}: {avg:.2f}")
        return avg
