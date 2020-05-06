def palin_perm(s):
    d = {x: 0 for x in range(128)}
    for char in s:
        if char != " ":
            d[ord(char)] += 1
    count = 0
    for key in d:
        if d[key] % 2 != 0:
            count += d[key] % 2
            if count > 1:
                return False
    return True


if __name__ == "__main__":
    print(palin_perm("tact coa"))
    print(palin_perm("code"))

# Time complexity O(n), space complexity O(1)
