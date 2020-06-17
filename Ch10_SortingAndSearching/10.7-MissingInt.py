def missing_int(arr):
    arr.sort()
    if arr[-1] != len(arr):
        return len(arr)
    if arr[0] != 0:
        return 0

    for i in range(1, len(arr)):
        expected_num = arr[i-1] + 1
        if arr[i] != expected_num:
            return expected_num


def missing_int_hash(arr):
    num_set = set(arr)
    n = len(arr) + 1
    for number in range(n):
        if number not in num_set:
            return number


if __name__ == "__main__":
    arr = [3, 0, 1]
    print(missing_int(arr))
    print(missing_int_hash(arr))
