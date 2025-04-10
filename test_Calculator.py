import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_mod(self):
        self.assertEqual(self.calc.mod(10, 3), 1)

    def test_mod_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.mod(10, 0)


if __name__ == '__main__':
    unittest.main()
    