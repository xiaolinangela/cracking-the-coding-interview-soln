def magic_index(array, start, end):
    mid_index = (start + end) // 2
    print(("array:{0}").format(array))
    print(("midindex:{0}").format(mid_index))
    if array[mid_index] == mid_index:
        return mid_index
    elif mid_index > array[mid_index]:
        return magic_index(array, mid_index+1, end)
    else:
        return magic_index(array, start, mid_index)


def magic_index_distinct(array, start, end):
    if end < start:
        return False
    mid_index = (start + end) // 2
    mid_value = array[mid_index]
    if array[mid_index] == mid_index:
        return mid_index
    left_index = min(mid_index-1, mid_value)
    left = magic_index_distinct(array, start, left_index)
    # print(left)
    if left:
        return left
    right_index = max(mid_index+1, mid_value)
    right = magic_index_distinct(array, right_index, end)
    return right


if __name__ == "__main__":
    # array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]

    # print(magic_index(array, start, end))
    array = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    start = 0
    end = len(array)-1
    print(magic_index_distinct(array, start, end))
