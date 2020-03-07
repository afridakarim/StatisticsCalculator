from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDev import *
from Statistics.Variance import *


class Statistics(Calculator):
    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def stdDevPop(self,data):
        self.result = StdDevPop(data)
        return self.result
    def stdDevSample(self,data):
        self.result = StdDevSample(data)
        return self.result

    def sampleVar(self,data):
        self.result = sampleVar(data)
        return self.result
    def popVar(self,data):
        self.result = popVar(data)
        return self.result