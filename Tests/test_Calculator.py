import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_return_difference(self):
        result = self.calculator.subtract(2, 2)
        self.assertEqual(0, result)

    def test_calculator_return_product (self):
        result = self.calculator.product(2,2)
        self.assertEqual(4,result)

    def test_calculator_return_division (self):
        result = self.calculator.division(2,2)
        self.assertEqual(1,result)

    def test_calculator_return_square (self):
        result = self.calculator.square(2)
        self.assertEqual(4,result)

    def test_calculator_return_SquareRoot(self):
        result = self.calculator.sqrt(4)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()