def search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] >= array[start]:
            if target >= array[start] and target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= array[end] and target > array[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == "__main__":
    array = [4, 5, 6, 7, 0, 1, 2]
    print(search(array, 0))
