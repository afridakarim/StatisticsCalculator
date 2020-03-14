from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.product import product
from Calculator.Division import division
from Calculator.Square import square
from Calculator.root import Root




class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def product(self,a,b):
        self.result = product(a,b)
        return self.result

    def division(self,a,b):
        self.result = division(a,b)
        return self.result

    def square(self,s):
        self.result = square(s)
        return self.result

    def sqrt(self,a):
        self.result = Root(a)
        return self.result
