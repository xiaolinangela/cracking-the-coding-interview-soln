def is_substring(s1, s2):
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            s1_sub = s1[i:(i+len(s2))]
            if s1_sub == s2:
                return True
    return False


def string_rotation(s1, s2):
    length = len(s1)
    if length == len(s2) and length != 0:
        s1s1 = s1 + s1
        return is_substring(s1s1, s2)
    return False


if __name__ == "__main__":
    print(string_rotation("waterbottle", "erbottlewat"))
