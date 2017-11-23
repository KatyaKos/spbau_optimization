import numpy as np

__author__ = 'KatyaKos'


class SparseMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.rows = []
        for i in range(self.n):
            self.rows.append([])
            for j in range(self.m):
                self.rows[i].append((j, matrix[i][j]))
        self.columns = []
        for i in range(self.m):
            self.columns.append([])
            for j in range(self.n):
                self.columns[i].append((j, matrix[j][i]))

    def T(self):
        return SparseMatrix([[self.matrix[i][j] for i in range(self.n)] for j in range(self.m)])

    # A * vector
    def mult_vector_right(self, vector):
        if vector.m != 1:
            print('That is not vector')
            exit(1)
        if vector.n != self.m:
            print('Cannot multiply matrix %dx%d on vector $d', self.n, self.m, vector.n)
        res_vec = []
        for rows in self.rows:
            res = 0.0
            for (i, val) in rows:
                res += vector.columns[0][i][1] * val
            res_vec.append(res)
        return SparseMatrix([res_vec]).T()

    # vector * A
    def mult_vector_left(self, vector):
        if vector.n != 1:
            print('That is not vector')
            exit(1)
        if vector.m != self.n:
            print('Cannot multiply matrix %dx%d on vector $d', self.n, self.m, vector.m)
        res_vec = []
        for columns in self.columns:
            res = 0.0
            for (i, val) in columns:
                res += vector.rows[0][i][1] * val
            res_vec.append(res)
        return SparseMatrix([res_vec])

    def minus_vector(self, v2):
        if self.n == 1 and v2.n == 1 and self.m == v2.m:
            return SparseMatrix([[self.matrix[0][i] - v2.matrix[0][i] for i in range(self.m)]])
        elif self.m == 1 and v2.m == 1 and self.n == v2.n:
            return SparseMatrix([[self.matrix[i][0] - v2.matrix[i][0] for i in range(self.n)]]).T()
        print('Cannot subtract vector from matrix')
        exit(1)

    def plus_vector(self, v2):
        if self.n == 1 and v2.n == 1 and self.m == v2.m:
            return SparseMatrix([[self.matrix[0][i] + v2.matrix[0][i] for i in range(self.m)]])
        elif self.m == 1 and v2.m == 1 and self.n == v2.n:
            return SparseMatrix([[self.matrix[i][0] + v2.matrix[i][0] for i in range(self.n)]]).T()
        print('Cannot subtract vector from matrix')
        exit(1)

    def div_number(self, number):
        if number.n != 1 or number.m != 1:
            print('You are trying to divide on matrix')
            exit(1)
        n = number.matrix[0][0]
        return SparseMatrix([[self.matrix[i][j] / n for j in range(self.m)] for i in range(self.n)])


def solve(n, m, a, b):
    b = SparseMatrix([np.squeeze(np.asarray(a.T * b.T))]).T()
    a = SparseMatrix(np.squeeze(np.asarray(a.T * a)))
    x = SparseMatrix([[1 for i in range(m)]])
    r = b.minus_vector(a.mult_vector_right(x.T()))
    z = r
    for i in range(max(n, m)):
        alpha = r.T().mult_vector_right(r).div_number(a.mult_vector_right(z).T().mult_vector_right(z))
        x = x.plus_vector(z.mult_vector_right(alpha).T())
        prev_r = r
        r = r.minus_vector(a.mult_vector_right(z).mult_vector_right(alpha))
        betta = r.T().mult_vector_right(r).div_number(prev_r.T().mult_vector_right(prev_r))
        z = r.plus_vector(z.mult_vector_right(betta))
    return x.matrix
