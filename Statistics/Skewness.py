from scipy.stats import skew

def skewness(data):
    skewResult = skew(data)
    return skewResult