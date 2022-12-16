def calculate_polska(s):
    stack = []
    for ch in s:
        if ch.isdigit():
            stack.append(ch)
        elif ch == "+":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) + int(y))
        elif ch == "-":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) - int(y))
        elif ch == "*":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) * int(y))
        elif ch == "/":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) / int(y))

    return stack.pop() if len(stack) == 1 else False


print(calculate_polska("234+*"))
