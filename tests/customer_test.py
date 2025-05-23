import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Customer(name="K" * 20)  
        c = Customer(name="Kelly")
        self.assertEqual(c.name, "Kelly")

if __name__ == "__main__":
    unittest.main()
