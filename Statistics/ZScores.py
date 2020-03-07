import scipy
from scipy import stats
from scipy.stats import zscore
from statistics import mean
from Statistics.Variance import popVar

def zValues(data):
    zVal = []
    for i in data:
        Z = (i - mean(data)) / (popVar(data))
        zVal.append(Z)
    return zVal


def zScores(zVal):
    zScores = []
    for i in zVal:
        zScores.append(scipy.stats.norm.cdf(i))
    return zScores

