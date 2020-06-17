def search(matrix, target):
    if matrix == []:
        return 0

    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1

    return False


if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(search(matrix, 3))
