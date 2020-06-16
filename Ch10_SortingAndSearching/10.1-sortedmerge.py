def sorted_merge(nums1, m, nums2, n):
    index1 = m - 1
    index2 = n - 1
    index_merged = m + n - 1
    while index2 >= 0:
        if index1 >= 0 and nums1[index1] > nums2[index2]:
            nums1[index_merged] = nums1[index1]
            index1 -= 1
        else:
            nums1[index_merged] = nums2[index2]
            index2 -= 1

        index_merged -= 1
    return nums1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    print(sorted_merge(nums1, m, nums2, n))

# Time Complexity: O(m+n)
# Space Complexity: O(1)
