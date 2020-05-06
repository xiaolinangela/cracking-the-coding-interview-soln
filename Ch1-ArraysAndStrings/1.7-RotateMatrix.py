def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(int(n/2)):
        first = layer
        last = n-layer-1
        for i in range(first, last):
            offset = i-first
            # save top
            top = matrix[i][first]
            # left to top
            matrix[i][first] = matrix[last][i]
            # top to right
            matrix[last][i] = matrix[last-offset][last]
            # right to bottom
            matrix[last-offset][last] = matrix[first][last-offset]
            # top to bottom
            matrix[first][last-offset] = top
    return matrix


if __name__ == "__main__":
    a = [[1, 2, 3], [1, 2, 3], [
        1, 2, 3]]

    print(rotate_matrix(a))
