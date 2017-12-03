import numpy as np
import math

__author__ = 'KatyaKos'


def heavy_ball(f, df, steps, x0, y0, l, L):
    sql = math.sqrt(l)
    sqL = math.sqrt(L)
    alpha = 4.0 / ((sql + sqL) ** 2)
    b = (sqL - sql) / (sql + sqL)
    xy = np.array([x0, y0])
    dxy = np.array([0, 0])
    for _ in range(steps):
        prev_x = xy.copy()
        xy = xy - alpha * df(xy[0], xy[1]) + b * dxy
        dxy = xy - prev_x
    vf = f(xy[0], xy[1])
    return xy, vf


def nesterov(f, df, steps, x0, y0, l, L):
    sql = math.sqrt(l)
    sqL = math.sqrt(L)
    b = (sqL - sql) / (sql + sqL)
    x = np.array([x0, y0])
    y = np.array([x0, y0])
    for _ in range(steps):
        prev_x = x
        x = y - df(y[0], y[1]) / L
        y = x + b * (x - prev_x)
    return x, y, f(x[0], x[1])


def chebushev(f, steps, xy0, l, L):
    e = np.array([[1.0, 0.0], [0.0, 1.0]])
    a = np.array([[l, 0.0], [0.0, L]])
    args = [np.array([(l + L) / (L - l)]), ((l + L) * e - 2 * a) / (L - l)]
    t = [[np.array([1]), args[0]], [e, args[1]]]
    x = np.dot(t[1][1], xy0) / t[0][1]
    for i in range(2, steps + 1):
        t[1].append(np.dot(2 * args[1], t[1][i - 1]) - t[1][i - 2])
        t[0].append(2 * args[0] * t[0][i - 1] - t[0][i - 2])
        x = np.dot(t[1][i], xy0) / t[0][i]
    return x, f(x[0], x[1])