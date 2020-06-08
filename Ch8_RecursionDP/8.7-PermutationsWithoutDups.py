import copy


def perm(nums):
    if len(nums) == 0:
        result = []
        return result
    result = perm(nums[0:len(nums)-1])
    new_result = []
    if len(result) == 0:
        result.append([nums[-1]])
        return result
    else:
        for i in result:
            for j in range(len(nums)):
                a = copy.copy(i)
                a.insert(j, nums[-1])
                new_result.append(a)
        return new_result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(perm(nums))
