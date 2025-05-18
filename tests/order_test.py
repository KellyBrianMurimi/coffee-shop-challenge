import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation_and_price(self):
        c = Customer("Beth")
        coffee = Coffee("Latte")
        o = Order(c, coffee, 4.5)
        self.assertEqual(o.customer.name, "Beth")
        self.assertEqual(o.coffee.name, "Latte")
        self.assertEqual(o.price, 4.5)

    def test_invalid_price(self):
        c = Customer("Ray")
        coffee = Coffee("Flat White")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)

if __name__ == "__main__":
    unittest.main()

