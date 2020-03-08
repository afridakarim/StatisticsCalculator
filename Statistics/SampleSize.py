from scipy import stats
from Calculator.Multiplication import product
from Calculator.Square import square
from Calculator.Division import division
from Statistics.ZScores import *
from Statistics.StandardDev import StdDevSample
from Statistics.MarginError import marginErr
from Statistics.ConfidenceInterval import c_i

def cochranSample(data):
    p = 0.5
    q = 1 - p
    p_q = product(p, q)
    List1 = []
    List2 = []
    for i in marginErr(data):
        List1.append(square(i))

    for i in zScores(zValues(data)):
        List2.append(square(i))
    i = 0
    n = []
    while i < len(List1):
        n.append(round(product(List1[i], p_q) / List2[i]))
        i += 1
    return n

def sample_yes_std(data):
    List1 = []
    List2 = []
    e = marginErr(data)
    k = c_i(data)
    for i in k:
        Z = i[1] / 2
        List1.append(scipy.stats.norm.cdf(Z))
    i = 0
    while i < len(List1):
        x = product(List1[i], StdDevSample(data))
        y = round(division(x, e[i]))
        List2.append((square(y)))
        i += 1
    return List2

def sample_no_std(data):
    e = marginErr(data)
    p = 0.5
    q = 1 - p
    p_q = product(q, p)
    List1 = []
    List2 = []
    x = c_i(data)
    for i in x:
        Z = i[1] / 2
        List1.append(scipy.stats.norm.cdf(Z))
    m_e = []
    for i in e:
        m_e.append(i / 2)
    i = 0
    while i < len(m_e):
        ZE = List1[i] / m_e[i]
        x = round(square(ZE) * p_q)
        List2.append(x)
        i += 1
    return List2


