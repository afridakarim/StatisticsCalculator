from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import Median
import pprint


class Statistics(Calculator):
    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = Median(data)
        return self.result
