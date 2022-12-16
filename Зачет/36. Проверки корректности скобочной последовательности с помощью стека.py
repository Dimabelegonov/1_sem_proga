def is_correct(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(1)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    return True


print(is_correct("(()(()))))"))
