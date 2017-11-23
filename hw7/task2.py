import numpy as np

__author__ = 'KatyaKos'


def solve(n):
    a = []
    for i in range(1, n + 1):
        a.append([])
        for j in range(1, n + 1):
            if (i + j) % 2 == 1:
                a[i - 1].append(0)
            else:
                a[i - 1].append(2/(i + j + 1))
    a = np.matrix(a)
    vec = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            vec.append(0)
        else:
            vec.append(-2/(i + 1))
    vec = np.matrix(vec)
    at = a.T
    return np.squeeze(np.asarray((at * a).I * at * vec.T))
