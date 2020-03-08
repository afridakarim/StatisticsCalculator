from statistics import mean
from Statistics.StandardDev import StdDevSample
from Statistics.ZScores import zScores
from Statistics.ZScores import zValues


def c_i(data):
    n = len(data)
    List = []
    std = StdDevSample(data)
    mu = mean(data)
    z_list = zScores(zValues(data))
    stdErr = std / n
    for i in z_list:
        lesser = mu - i * stdErr
        greater = mu + i * stdErr
        List.append([lesser, greater])
    return List