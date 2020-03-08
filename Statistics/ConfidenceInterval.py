from scipy.stats import sem, t
from Statistics.Mean import mean

confidence = 0.95

def c_i(data):
    n = len(data)
    m = mean(data)
    stdErr = sem(data)
    h = stdErr * t.ppf((1 + confidence) / 2, n - 1)
    start = m - h
    end = m + h
    return start, end