def find_dup(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]


if __name__ == "__main__":

    arr = [1, 5, 2, 4, 5]
    print(find_dup(arr))
