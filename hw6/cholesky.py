import math

__author__ = 'KatyaKos'


def find_diag_el(a, l, i):
    sums = 0
    for j in range(i):
        sums += l[i][j] * l[i][j]
    if a[i][i] <= sums:
        return -1
    return math.sqrt(a[i][i] - sums)


def find_el(a, l, i, j):
    sums = 0
    for k in range(j):
        sums += l[i][k]*l[j][k]
    if l[j][j] != 0:
        return (a[i][j] - sums) / l[j][j]
    else:
        return 1


def cholesky(a, n):
    l = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i):
            l[i][j] = find_el(a, l, i, j)
        l[i][i] = find_diag_el(a, l, i)
        if l[i][i] == -1:
            return []
    return l