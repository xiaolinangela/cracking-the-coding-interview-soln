def is_unique(string):
    char_set = [False for i in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val] == True:
            return print("False")
        else:
            char_set[val] = True

    return print("True")


if __name__ == "__main__":
    is_unique("sting!@")

# Space Complexity O(1). Time Complexity O(n)
