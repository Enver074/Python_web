# Напишите функцию для транспонирования матрицы

matrix = [[1, 3, 6],
          [2, 4, 8],
          [3, 6, 9]]


def matrix_transpose(mtrx):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(mtrx)):
        for x in range(len(mtrx[0])):
            result[x][i] = mtrx[i][x]

    print(result)

if __name__ == "__main__":
    matrix_transpose(matrix)