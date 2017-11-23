import numpy as np

__author__ = 'KatyaKos'


def solve(n, m, a, b):
    at = a.T
    a = at * a #m x m
    b = at * b.T #столбец размера m
    x = np.matrix([1 for i in range(m)])
    r = b - a * x.T #стобец размера m
    z = r
    for i in range(max(n, m)):
        alpha = np.dot(r.T, r) / np.dot(np.dot(a, z).T, z)
        x = x + np.dot(alpha, z.T)
        prev_r = r
        r = r - np.dot(alpha, np.dot(a, z).T).T
        betta = np.dot(r.T, r) /np.dot(prev_r.T, prev_r)
        z = r + np.dot(betta, z.T).T
    return np.squeeze(np.asarray(x))
