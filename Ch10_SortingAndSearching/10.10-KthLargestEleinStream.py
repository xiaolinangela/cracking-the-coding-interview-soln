import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]


if __name__ == "__main__":
    arr = [4, 5, 8, 2]
    kth = KthLargest(3, arr)
    print(kth.add(3))
    print(kth.add(5))
