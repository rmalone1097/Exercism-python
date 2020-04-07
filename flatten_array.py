def flatten(iterable):
    oneD = []
    for entry in iterable:
        if isinstance(entry, list) and entry is not None:
            oneD += flatten(entry)
        elif entry is not None:
            oneD.append(entry)
    return oneD

print(flatten([0, 2, [[2,3], 8, 100, 4, [[[None]]]], -2]))