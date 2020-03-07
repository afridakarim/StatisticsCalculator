import numpy as np


def qrt1(data):
    q1 = np.quantile(data, 0.25)
    return q1

def qrt2(data):
    q2 = np.quantile(data, 0.50)
    return q2

def qrt3(data):
    q3 = np.quantile(data, 0.75)
    return q3
