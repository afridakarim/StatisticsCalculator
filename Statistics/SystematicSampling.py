def systematic_sampling(data):
    sysList = []

    sysValue = len(data) / 5
    i = 0
    while i < len(data):
        sysList.append(i)
        i = float(i + sysValue)
    return sysList