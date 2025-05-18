class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        print(f"Customer created: {self._name}")

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
        print(f"{self._name}'s orders: {self._orders}")
        return self._orders

    def coffees(self):
        coffee_list = list(set(order.coffee for order in self._orders))
        print(f"{self._name} has ordered these coffees: {[c.name for c in coffee_list]}")
        return coffee_list

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        print(f"{self._name} created an order: {coffee.name} at ${price}")
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        spending = {}
        for order in coffee.orders():
            customer = order.customer
            spending[customer] = spending.get(customer, 0) + order.price
            print(f"{customer.name} spent ${order.price} on {coffee.name} (total: ${spending[customer]})")
        
        if spending:
            aficionado = max(spending, key=spending.get)
            print(f"Most aficionado for {coffee.name}: {aficionado.name} with ${spending[aficionado]}")
            return aficionado
        else:
            print(f"No aficionados for {coffee.name}")
            return None
