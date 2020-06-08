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
            j = 0
            while j < len(nums):
                a = copy.copy(i)
                a.insert(j, nums[-1])
                new_result.append(a)
                if nums[-1] == i[j-1]:
                    j += 2
                else:
                    j += 1
        # print(new_result)
        return new_result


if __name__ == "__main__":
    nums = [2, 2, 1, 1]
    print(perm(nums))

122 212 221    1122 1212 1221
