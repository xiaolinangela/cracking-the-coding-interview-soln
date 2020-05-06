def check_permutation_opt(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        d = {x: 0 for x in range(128)}
        for char1 in str1:
            d[ord(char1)] += 1
        for char2 in str2:
            d[ord(char2)] -= 1
            if d[ord(char2)] < 0:
                return False
        return True


if __name__ == "__main__":
    if check_permutation_opt('wef34f', 'wfff34'):
        print("str1 is permutation of str2")
    else:
        print("str1 is not permutation of str2")

    if check_permutation_opt('2354', '1234'):
        print("str1 is permutation of str2")
    else:
        print("str1 is not permutation of str2")
