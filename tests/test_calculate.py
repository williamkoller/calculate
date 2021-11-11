import unittest
from calculate.calculation import Calculation


class TestCalculate(unittest.TestCase):

    def test_return_calculation_sum(self):
        self.assertEqual(Calculation.addition(10, 10), 20)

    def test_return_calculation_subtraction(self):
        self.assertEqual(Calculation.subtraction(40, 20), 20)

    def test_return_calculation_division(self):
        self.assertEqual(Calculation.division(10, 2), 5)

    def test_return_calculation_multiplication(self):
        self.assertEqual(Calculation.multiplication(10, 10), 100)

    def test_return_calculation_power(self):
        self.assertEqual(Calculation.power(2, 3), 8)
