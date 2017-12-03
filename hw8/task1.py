import numpy as np
from hw8.methods import heavy_ball, nesterov, chebushev

__author__ = 'KatyaKos'


def f(x, y):
    return 0.5 * (x ** 2 + 69 * y ** 2)


def df(x, y):
    return np.array([x, 69 * y])


def task1(type, steps, x0, y0, l, L):
    if type == 0:
        return heavy_ball(f, df, steps, x0, y0, l, L)
    elif type == 1:
        return nesterov(f, df, steps, x0, y0, l, L)
    else:
        return chebushev(f, steps, np.array([x0, y0]), l, L)
