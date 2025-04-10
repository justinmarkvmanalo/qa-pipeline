import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 9), 11)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(15, 7), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 4), 24)

    def test_divide(self):
        self.assertEqual(self.calc.divide(12, 3), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(7, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(3, 4), 81)

    def test_mod(self):
        self.assertEqual(self.calc.mod(20, 6), 2)

    def test_mod_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.mod(15, 0)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(25), 5)
        self.assertEqual(self.calc.sqrt(9), 3)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-16)


if __name__ == '__main__':
    unittest.main()
    