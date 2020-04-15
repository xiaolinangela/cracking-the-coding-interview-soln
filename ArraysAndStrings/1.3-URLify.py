import time
start_time = time.time()


def URLify(str, trueLength):
    list_str = list(str)
    list_str = list_str[:trueLength]
    for i in range(trueLength):
        if list_str[i] == " ":
            list_str[i] = "%20"
    url_str = "".join(list_str)
    return url_str


def URLify_simple(str, trueLength):
    return str.strip().replace(" ", "%20")


if __name__ == "__main__":
    print(URLify("Mr John Smith    ", 13))

print("--- %s seconds ---" % (time.time() - start_time))
