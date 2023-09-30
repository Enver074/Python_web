class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def trans_zip(self):
        return list(zip(* self.matrix))


mtrx = [[1, 3, 6],
          [2, 4, 8],
          [3, 6, 9]]

print(Matrix.trans_zip(Matrix(mtrx)))
