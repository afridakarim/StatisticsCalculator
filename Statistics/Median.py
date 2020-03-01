from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code



def median(data):
    n = len(data)
    median = n // 2
    if n % 2 == 0:
        middle = (data[median] + data[median - 1]) / 2
    else:
        middle = data[median]

    return middle
