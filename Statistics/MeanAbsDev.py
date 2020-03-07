from numpy import mean, absolute

def meanDev(data):
    m_a_d = mean(data - mean(data))
    return m_a_d

def meanAbsDev(data):
    m_a_d = mean(absolute(data - mean(data)))
    return m_a_d