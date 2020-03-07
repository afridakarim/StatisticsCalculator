import math
from Statistics.Mean import mean
from Calculator.Square import square


def StdDevSample(data):
    Sum1 = 0
    for i in data:
        x = abs(i - mean(data))
        Sum1 = square(x) + Sum1
    n = len(data)
    stdDev = math.sqrt(Sum1 / (n - 1))
    return stdDev


def StdDevPop(data):
    Sum2 = 0
    for i in data:
        x = abs(i - mean(data))
        Sum2 = square(x) + Sum2
    n = len(data)
    stdDev = math.sqrt(Sum2) / n
    return stdDev
