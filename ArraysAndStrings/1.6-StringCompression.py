def stringCompression(str1):
    result = []
    count = 0
    list_str1 = list(str1)
    for i in range(0, len(list_str1)):
        count += 1
        if i+1 == len(str1) or list_str1[i+1] != list_str1[i]:
            result.append(list_str1[i])
            result.append(str(count))
            count = 0
    return min(''.join(result), str1, key=len)


if __name__ == "__main__":
    print(stringCompression("aaabbb"))
