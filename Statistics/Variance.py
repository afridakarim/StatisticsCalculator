from Statistics.StandardDev import *
from Calculator.root import Root

def sampleVar(data):
    x = StdDevSample(data)
    return Root(x)

def popVar(data):
    x = StdDevPop(data)
    return Root(x)