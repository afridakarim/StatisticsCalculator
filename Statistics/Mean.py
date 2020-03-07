from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    total = 0
    num_values = len(data)
    for num in data:
        total = addition(total, num)
    return division(num_values, total)






