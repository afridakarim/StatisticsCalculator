from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    total = 0
    num_values = len(data)
    for i in data:
        total = addition(total, i)
    return division(num_values, total)






