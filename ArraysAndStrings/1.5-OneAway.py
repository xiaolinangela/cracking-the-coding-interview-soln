def OneAway(first, second):
    # print(abs(len(s1)-len(s2)))
    if abs(len(first)-len(second)) > 1:
        return False
    if len(first) > len(second):
        long_str = first
        short_str = second
    else:
        long_str = second
        short_str = first
    index_long = 0
    index_short = 0
    founddiff = False
    while (index_long < len(long_str) and index_short < len(short_str)):
        if(long_str[index_long] != short_str[index_short]):
            if (founddiff):
                return False
            founddiff = True
            if len(long_str) == len(short_str):
                index_short += 1
        else:
            index_short += 1
        index_long += 1
    return True


if __name__ == "__main__":
    print(OneAway("pale", "psli"))
    print(OneAway("pale", "pal"))
    print(OneAway("pal", "peal"))
    print(OneAway("pil", "peal"))
