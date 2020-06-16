from collections import defaultdict


def group_anagrams(strs):
    htable = defaultdict(list)
    for word in strs:
        htable["".join(sorted(word))].append(word)
    return htable.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))


# Time Complexity: O(KlogK) K is the maximum length of a string in strs.
# Space Complexity: O(NK)
