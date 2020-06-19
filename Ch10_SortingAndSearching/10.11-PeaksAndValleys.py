def pv(arr):
    peak = []
    valley = []
    i = 0
    while i < len(arr) - 1:
        while i < len(arr) - 1 and arr[i] >= arr[i+1]:
            i += 1
        valley.append(arr[i])
        while i < len(arr) - 1 and arr[i] <= arr[i+1]:
            i += 1
        peak.append(arr[i])

    return peak, valley


if __name__ == "__main__":
    arr = [5, 8, 6, 2, 3, 4, 6]
    print(pv(arr))


# Time Complexity O(n)
# Space Complexity O(1)
