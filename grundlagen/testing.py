import unittest
from main import calculate_price

class TestPriceCalculation(unittest.TestCase):
    def test_basic_calculation(self):
        price = calculate_price(1000, 200, 300, 4, 10)
        expected_price = 1000 * 0.9 + 200 + 300 * 0.9
        self.assertEqual(price, expected_price, f"Expected {expected_price}, but got {price}.")

if __name__ == '__main__':
    unittest.main()
