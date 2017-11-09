import math
import random

__author__ = 'KatyaKos'


def f(x, y):
    if FUNC_TYPE == 1:
        return (x * x + 69 * y * y) / 2
    else:
        return math.exp(x + 3 * y - 0.1) + math.exp(x - 3 * y - 0.1) + math.exp(-x - 0.1)


def df(x, y):
    if FUNC_TYPE == 1:
        return x, 69 * y
    else:
        return math.exp(x + 3 * y - 0.1) + math.exp(x - 3 * y - 0.1) - math.exp(-x - 0.1), \
               3 * math.exp(x + 3 * y - 0.1) - 3 * math.exp(x - 3 * y - 0.1)


def norm(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def real_min():
    if FUNC_TYPE == 1:
        return 0, 0
    else:
        return -math.log(2) / 2, 0


def move(x, y, a):
    dx, dy = df(x, y)
    return x - a * dx, y - a * dy


def get_value(x, y, a):
    new_x, new_y = move(x, y, a)
    return f(new_x, new_y)


def ternary(x, y):
    l = -1
    r = 1
    while r - l > 1e-6:
        m1 = 2 / 3 * l + r / 3
        m2 = l / 3 + 2 / 3 * r
        f1 = get_value(x, y, m1)
        f2 = get_value(x, y, m2)
        if f1 < f2:
            r = m2
        elif f1 > f2:
            l = m1
        else:
            l = m1
            r = m2
    return random.uniform(l, r)


def backtracking(x, y):
    a = 1
    gamma = 1e-6 + random.uniform(0, 1 / 2)
    betta = 1e-6 + random.uniform(0, 1)
    dx, dy = df(x, y)
    norm_sq = norm(dx, dy, 0, 0) ** 2
    new_x, new_y = move(x, y, a)
    while f(new_x, new_y) > f(x, y) - gamma * a * norm_sq:
        a *= betta
        new_x, new_y = move(x, y, a)
    return a


def alpha(x, y):
    if GRAD_TYPE == 1:
        return 1 / 100
    elif GRAD_TYPE == 2:
        return ternary(x, y)
    else:
        return backtracking(x, y)


def gradient_descent():
    random.seed()
    cur_x = x0
    cur_y = y0
    i = 0
    min_x, min_y = real_min()
    norm_v = norm(cur_x, cur_y, min_x, min_y)
    f_diff = f(cur_x, cur_y) - f(min_x, min_y)
    while norm_v >= EPS:
        print('step=', i, ', x=', cur_x, ', y=', cur_y, ', ||xi - x*||=', norm_v, ', f(xi)-f(x*)=', f_diff, ';', sep='')
        norm_v = norm(cur_x, cur_y, min_x, min_y)
        f_diff = f(cur_x, cur_y) - f(min_x, min_y)
        a = alpha(cur_x, cur_y)
        cur_x, cur_y = move(cur_x, cur_y, a)
        i += 1
    print('step=', i, ', x=', cur_x, ', y=', cur_y, ', ||xi - x*||=', norm_v, ', f(xi)-f(x*)=', f_diff, ';', sep='')


print('enter x0')
x0 = float(input())
print('enter y0')
y0 = float(input())
print('enter epsilon')
EPS = float(input())
print('enter task number: 1 or 2')
FUNC_TYPE = int(input())
print('enter method type: 1, 2 or 3')
GRAD_TYPE = int(input())
gradient_descent()
