number_till = 5


def define_matrix(matrix, m, n):
    f = open('numbers.txt', 'r+')
    matrix2 = [[1 for i in range(0, m)] for j in range(0, n)]
    for i in range(m):
        for j in range(n):
            # print (int(f.read(2).strip()), '\t', end='')
            matrix2[i][j] = int(f.read(3).strip())
            # print('')

    return matrix2


def print_matrix(matrix, m, n):
    for i in range(0, m, 1):
        for j in range(0, n, 1):
            print(' ', matrix[m][n], end='')
        print('')


def forward_search(matrix, m, n):
    highest = 0
    for i in range(m):
        for j in range(n - number_till):
            temp = 1
            for k in range(0, number_till - 2, 1):
                temp = temp * matrix[i][j + k]
                print('i, j, k', i, j, k)
            if temp > highest:
                highest = temp
    return highest


def downward_search(matrix, m, n):
    highest = 0
    for i in range(m - number_till):
        for j in range(n):
            temp = 1
            for k in range(0, number_till - 1, 1):
                temp = temp * matrix[i + k][j]
                print('i, j, k', i, j, k)
            if temp > highest:
                highest = temp
    return highest


def diagonal_search(matrix, m, n):
    highest = 0
    for i in range(m - number_till + 2):
        for j in range(n - number_till + 2):
            temp = 1
            for k in range(0, number_till - 1, 1):
                temp = temp * matrix[i + k][j + k]
                print('i, j, k', i, j, k)
            if temp > highest:
                highest = temp
    return highest


matrix = [[1 for i in range(0, 19)] for j in range(0, 19)]
matrix = define_matrix(matrix, 20, 20)
print(matrix)
forw = forward_search(matrix, 20, 20)
down = downward_search(matrix, 20, 20)
diag = diagonal_search(matrix, 20, 20)
print(forw, diag, down)