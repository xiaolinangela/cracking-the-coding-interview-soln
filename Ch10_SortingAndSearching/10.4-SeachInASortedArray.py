def search(array, target):
    left, right = 0, 1
    while array.get(right) < target:
        left = right
        right = right * 2

    while left <= right:
        mid = left + (right-left) // 2
        if array.get(mid) == target:
            return mid
        elif target < array.get(mid):
            right = mid - 1
        else:
            left = mid + 1

    return -1
