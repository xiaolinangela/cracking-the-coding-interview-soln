def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    if check_permutation("geeksforgeeks", "forgeeksgeeks"):
        print("str1 is permutation of str2")
    else:
        print("str1 is not permutation of str2")

    if check_permutation("allergy", "allergicy"):
        print("str1 is permutation of str2")
    else:
        print("str1 is not permutation of str2")
