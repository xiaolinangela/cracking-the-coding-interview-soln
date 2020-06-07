def recursive_multiply(a, b):
    if b == 0 or a == 0:
        return 0
    if b == 1:
        return a
    return a + recursive_multiply(a, b-1)


def rm_bottomup(a, b):
    if b == 0:
        return 0
    result = [0] * (b+1)
    print(result)
    result[1] = a
    for i in range(2, b+1):
        result[i] = result[i-1] + a
    return result[b]


if __name__ == "__main__":
    print(rm_bottomup(8, 4))
