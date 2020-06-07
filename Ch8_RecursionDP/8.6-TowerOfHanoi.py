def TowerOfHanoi(n, source, target, aux):
    if n > 0:
        TowerOfHanoi(n-1, source, aux, target)
        target.append(source.pop())
        TowerOfHanoi(n-1, aux, target, source)
    print(target)


if __name__ == "__main__":
    A = [1, 2, 3]
    B = []
    C = []
    TowerOfHanoi(3, A, C, B)
