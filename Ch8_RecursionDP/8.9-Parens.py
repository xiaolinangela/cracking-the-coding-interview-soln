def generateParenthesis(n):
    def insertInside(str, left_index):
        left = str[:left_index+1]
        right = str[left_index+1:]
        return left + "()" + right
    if n == 1:
        result = {"()"}
        return result
    else:
        result = generateParenthesis(n-1)
        new_result = set()
        for str in result:
            for i in range(len(str)):
                if str[i] == "(":
                    s = insertInside(str, i)
                    new_result.add(s)
            new_result.add("()" + str)
        return new_result


if __name__ == "__main__":
    print(generateParenthesis(3))
