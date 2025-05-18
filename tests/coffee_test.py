import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("ab")
        c = Coffee("Latte")
        self.assertEqual(c.name, "Latte")

if __name__ == "__main__":
    unittest.main()

