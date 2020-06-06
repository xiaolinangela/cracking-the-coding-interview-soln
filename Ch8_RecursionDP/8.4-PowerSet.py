def power_set(nums):
    output = [[]]
    for num in nums:
        output += [curr + [num] for curr in output]
    return output


if __name__ == "__main__":
    s = [1, 2, 3]
    print(power_set(s))
