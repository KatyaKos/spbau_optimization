from hw6.cholesky import cholesky
from hw6.task3 import check_invertible, solve
import numpy as np
import matplotlib.pyplot as plt

__author__ = 'KatyaKos'


def f(kp, xx):
    res = 0
    for i in range(len(kp)):
        res += kp[i] * (xx ** ii)
    return res


def draw(xmin, xmax, kp):
    fig = plt.figure(figsize=(20, 20))
    ax = fig.gca()
    x = np.arange(xmin, xmax, 0.1)
    y = f(kp, x)
    plt.plot(x, y)
    plt.yticks(np.arange(np.min(y) - 5, np.max(y) + 5, 5))
    ax.scatter(x, y)
    plt.show()


print('Enter number of task: 1-3')
task = int(input())
if task == 1:
    nn = int(input())
    mat = []
    for ii in range(nn):
        mat.append([int(j) for j in input().split()])
        if len(mat[ii]) != nn:
            print('input is not correct')
            exit(1)
    res = cholesky(mat, nn)
    if not res:
        print('not positive definite')
    else:
        for row in res:
            for el in row:
                print('{0:15f}'.format(el), end='')
            print()
elif task == 2:
    n = int(input())
    m = int(input())
    x = [int(xi) for xi in input().split()]
    y = [int(yi) for yi in input().split()]
    if len(x) != m or len(y) != m:
        print('input is not correct')
        exit(0)
    matx = []
    for ii in range(m):
        matx.append([])
        for jj in range(n + 1):
            matx[ii].append(x[ii] ** jj)
    kp = solve(np.matrix(matx), np.matrix(y))
    for ii in range(len(kp)):
        print('p', ii, '=', kp[ii], sep='')
    draw(np.min(x) - 2, np.max(x) + 2, kp)
else:
    n = int(input())
    m = int(input())
    a = []
    for ii in range(n):
        a.append([int(j) for j in input().split()])
        if len(a[ii]) != m:
            print('input is not correct')
            exit(1)
    b = [int(bi) for bi in input().split()]
    if len(b) != n:
        print('input is not correct')
        exit(1)
    if check_invertible(np.matrix(a), m):
        x = solve(np.matrix(a), np.matrix(b))
        for ii in range(len(x)):
            print('x', ii, '=', x[ii], sep='')
    else:
        print('bad input')
