from Statistics.StandardDev import StdDevSample
from Statistics.ZScores import *
from Calculator.root import Root

def marginErr(data):
    nList = []
    stdErr = (StdDevSample(data) / Root((len(data))))
    for i in zScores(zValues(data)):
        marginErr = i * stdErr
        nList.append(marginErr)

    return nList
