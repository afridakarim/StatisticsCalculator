from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code
import pprint


def mean(data):
    total = 0
    num_values = len(data)
    for num in data:
        total = addition(total, num)
    return division(num_values, total)






