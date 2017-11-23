from hw7.task1 import orthogonal_basis, dual_basis
from hw7 import task2, task3, task4
import numpy as np

__author__ = 'KatyaKos'


def check_solution(a, b, x):
    a = np.matrix(a)
    b = np.matrix(b)
    x = np.matrix(x)
    print('Enter epsilon to check solution')
    eps = float(input())
    return np.linalg.norm(a * x.T - b.T) < eps


print('Enter number of task: 1-5')
task = int(input())
if task == 1:
    print('Enter m: number of vectors')
    m = int(input())
    print('Enter n: dimension')
    n = int(input())
    print('Enter vectors')
    v = []
    for ii in range(m):
        v.append([float(j) for j in input().split()])
        if len(v[ii]) != n:
            print('input is not correct')
            exit(1)
    print('Enter matrix A')
    a = []
    for ii in range(n):
        a.append([float(j) for j in input().split()])
        if len(a[ii]) != n:
            print('input is not correct')
            exit(1)

    print('Orthogonal basis for vectors:')
    print(orthogonal_basis(v))
    print('A-orthogonal basis:')
    print(dual_basis(v, np.matrix(a)))
elif task == 2:
    print('Enter n')
    n = int(input())
    print('Alpha values are:')
    print(task2.solve(n))
elif task == 3 or task == 4:
    print('A = Mat(n x m), b = R^n')
    print('Enter n dimension')
    n = int(input())
    print('Enter m dimension')
    m = int(input())
    print('Enter matrix A')
    a = []
    for ii in range(n):
        a.append([float(j) for j in input().split()])
        if len(a[ii]) != m:
            print('input is not correct')
            exit(1)
    print('Enter vector b')
    b = [float(bi) for bi in input().split()]
    if len(b) != n:
            print('input is not correct')
            exit(1)
    res = 0
    if task == 3:
        res = task3.solve(n, m, np.matrix(a), np.matrix(b))
    else:
        res = task4.solve(n, m, np.matrix(a), np.matrix(b))
    if check_solution(a, b, res):
        print(res)
    else:
        print('No solution')
else:
    print('Enter number of vertexes')
    n = int(input())
    print('Enter number of edges')
    m = int(input())
    print('Enter incidence matrix')
    a = []
    for ii in range(n):
        a.append([float(j) for j in input().split()])
        if len(a[ii]) != m:
            print('input is not correct')
            exit(1)
    print('Enter vector')
    b = [float(bi) for bi in input().split()]
    if len(b) != n:
            print('input is not correct')
            exit(1)
    res = task4.solve(n, m, np.matrix(a), np.matrix(b))
    if check_solution(a, b, res):
        print(res)
    else:
        print('No solution')
