def triple_step(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    bottom_up = [0] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 2
    bottom_up[3] = 4
    for i in range(4, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2] + bottom_up[i-3]
    return bottom_up[n]


if __name__ == "__main__":
    print(triple_step(4))
