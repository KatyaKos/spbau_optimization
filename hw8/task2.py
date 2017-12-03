import numpy as np
import math
from hw8.methods import nesterov

__author__ = 'KatyaKos'


def f(x, y):
    return math.exp(x + 3 * y - 0.1) + math.exp(x - 3 * y - 0.1) + math.exp(-x - 0.1)


def df(x, y):
    return np.array([
        math.exp(x + 3 * y - 0.1) + math.exp(x - 3 * y - 0.1) - math.exp(-x - 0.1),
        3 * math.exp(x + 3 * y - 0.1) - 3 * math.exp(x - 3 * y - 0.1)
    ])


def task2(steps, x0, y0, l, L):
    max_x = max(1, abs(x0))
    max_y = max(1, abs(y0))
    for _ in range(1000):
        xes = np.random.random([4])
        p = np.array([max_x * (2 * xes[0] - 1), max_y * (2 * xes[1] - 1)])
        pp = np.array([max_x * (2 * xes[2] - 1), max_y * (2 * xes[3] - 1)])
        dfp = (df(p[0], p[1]) - df(pp[0], pp[1])) * (p - pp)
        t = (dfp[0] + dfp[1]) / np.linalg.norm(p - pp) ** 2
        L = max(L, t)
        l = min(l, t)
        if l == 0:
            l = t
    return nesterov(f, df, steps, x0, y0, l / 2, L * 2), f(-math.log(2.0) / 2, 0.0)
