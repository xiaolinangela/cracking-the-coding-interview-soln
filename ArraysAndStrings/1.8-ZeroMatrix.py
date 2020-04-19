def zero_matrix(matrix):
    set_row = set()
    set_column = set()
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j in set_column and matrix[i][j] != 0:
                matrix[i][j] = 0
            elif matrix[i][j] == 0:
                set_row.add(i)
                set_column.add(j)
                for m in range(i):
                    matrix[m][j] = 0
        if i in set_row:
            matrix[i] = [0] * len(matrix[i])
    return matrix


def zero_matrix_space_opt(matrix):
    rowhaszeros = False
    colhaszeros = False
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            rowhaszeros = True
            break
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            colhaszeros = True
            break
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            matrix[i] = [0] * len(matrix[0])
        else:
            for j in range(len(matrix[0])):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
    if rowhaszeros:
        matrix[0] = [0] * len(matrix[0])
    if colhaszeros:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    return matrix


if __name__ == "__main__":
    print(zero_matrix_space_opt([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
