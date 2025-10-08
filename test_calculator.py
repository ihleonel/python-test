from unittest import TestCase
from main import Calculator


class TestCalculator(TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 2), 4)

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(3, 4), 12)

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)
        with self.assertRaises(Exception):
            calc.divide(1, 0)
