
from typing import List, Tuple


def greedy_sdm(sf: List[Tuple]) -> Tuple[List[Tuple], int]:
    _x = [sf[0]]
    i = 0
    iterations = 0
    for k in range(1, len(sf)):
        if sf[k][0] > sf[i][1]:
            _x.append(sf[k])
            i = k
        iterations += 1
    return _x, iterations


# s 4 6 13 4 2 6 7  9  1 3  9
# f 8 7 14 5 4 9 10 11 6 13 12
# X 0 1 1  0 1 0 0  1  0 0  0
interval = [(2, 4), (4, 5), (1, 6), (6, 7), (4, 8), (6, 9),
            (7, 10), (9, 11), (9, 12), (3, 13), (13, 14)]
print(greedy_sdm(interval))
