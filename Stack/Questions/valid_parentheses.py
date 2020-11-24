def valid_parentheses(s):
    if not s:
        return True
    elif len(s) == 1:
        return False

    d = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for bracket in s:
        if bracket in d:
            stack.append(bracket)
        elif d[stack.pop()] != bracket:
            return False

    return len(stack) == 0


if __name__ == "__main__":
    string = "[[{{}}]](())([])"
    print(valid_parentheses(string))