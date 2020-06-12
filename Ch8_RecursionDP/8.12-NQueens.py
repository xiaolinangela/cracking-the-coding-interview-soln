def n_queens(n):
    positions = [0 for x in range(n)]

    def helper(n, row, positions):
        if n == row:
            return True

        for col in range(n):
            foundSafe = True

            for queen in range(row):
                if positions[queen][1] == col or positions[queen][0] - positions[queen][1] == row-col or positions[queen][0] + positions[queen][1] == row + col:
                    foundSafe = False
                    break

            if foundSafe:
                positions[row] = [row, col]
                if helper(n, row+1, positions):
                    return True

        return False
    has_solution = helper(n, 0, positions)
    print(has_solution)
    if has_solution:
        return positions


if __name__ == "__main__":
    print(n_queens(8))
