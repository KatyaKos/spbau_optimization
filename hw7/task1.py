import numpy as np

__author__ = 'KatyaKos'


def proj(a, b):
    return np.dot((np.dot(a, b.T) / np.dot(b, b.T)), b)


def projA(v, u):
    uTa = np.dot(u, matrix)
    return np.dot(np.dot(uTa, v.T) / np.dot(uTa, u.T), u)


def orthogonal_basis(vectors):
    orth = [np.array(vectors[0])]
    for i in range(1, len(vectors)):
        a = np.array(vectors[i])
        b = a
        for j in range(i):
            b = b - proj(a, orth[j])
        orth.append(b)
    return orth


def dual_basis(vectors, ma):
    global matrix
    matrix = ma
    dual = [np.matrix(vectors[0])]
    for i in range(1, len(vectors)):
        v = np.matrix(vectors[i])
        u = v
        for j in range(i):
            u = u - projA(v, dual[j])
        dual.append(u)
    return dual
