from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDev import *
from Statistics.Variance import *
from Statistics.MeanAbsDev import *
from Statistics.ZScores import *
from Statistics.Correlation import *
from Statistics.Quartiles import *
from Statistics.MarginError import marginErr
from Statistics.SystematicSampling import systematic_sampling
from Statistics.Skewness import skewness
from Statistics.Correlation import *
from Statistics.ConfidenceInterval import c_i
from Statistics.SampleSize import *


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

    def stdDevPop(self, data):
        self.result = StdDevPop(data)
        return self.result

    def stdDevSample(self, data):
        self.result = StdDevSample(data)
        return self.result

    def sampleVar(self, data):
        self.result = sampleVar(data)
        return self.result

    def popVar(self, data):
        self.result = popVar(data)
        return self.result

    def meanDev(self, data):
        self.result = meanDev(data)
        return self.result

    def meanAbsDev(self, data):
        self.result = meanAbsDev(data)
        return self.result

    def zValues(self, data):
        self.result = zValues(data)
        return self.result

    def zScores(self, data):
        self.result = zScores(self.zValues(data))
        return self.result

    def sample_correlation_coeff(self, data):
        self.result = sampleCorrelation(data)
        return self.result
    def pop_correlation_coeff(self, data):
        self.result = populationCorrelation(data)
        return self.result

    def quart1(self, data):
        self.result = qrt1(data)
        return self.result

    def quart2(self, data):
        self.result = qrt2(data)
        return self.result

    def quart3(self, data):
        self.result = qrt3(data)
        return self.result

    def mErr(self, data):
        self.result = marginErr(data)
        return self.result

    def sys_samp(self, data):
        self.result = systematic_sampling(data)
        return self.result

    def skewness(self, data):
        self.result = skewness(data)
        return self.result

    def confidenceInterval(self, data):
        self.result = c_i(data)
        return self.result

    def cochran(self,data):
        self.result = cochranSample(data)
        return self.result

    def yes_std(self,data):
        self.result = sample_yes_std(data)
        return self.result

    def no_std(self,data):
        self.result = sample_no_std(data)
        return self.result