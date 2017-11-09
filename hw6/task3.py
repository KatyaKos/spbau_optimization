from hw6.cholesky import cholesky
import numpy as np

__author__ = 'KatyaKos'


def check_invertible(mat, m):
    l = cholesky(np.asarray(mat * mat.T), m)
    return l != []


def solve(aa, vec):
    at = aa.T
    return np.squeeze(np.asarray((at * aa).I * at * vec.T))
