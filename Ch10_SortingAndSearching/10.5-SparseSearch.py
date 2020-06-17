def search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == "":
            left = mid - 1
            right = mid + 1

            while True:
                if left < low and right > high:
                    return -1
                elif left >= low and arr[left] != "":
                    mid = left
                    break
                elif right <= high and arr[right] != "":
                    mid = right
                    break
                left -= 1
                right += 1

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1
    return -1


if __name__ == "__main__":
    arr = ["at", "", "", "", "ball", "", "car"]
    print(search(arr, "gall"))
