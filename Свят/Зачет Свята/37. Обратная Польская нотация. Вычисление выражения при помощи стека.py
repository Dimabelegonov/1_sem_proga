"""
Обратная польская запись  — форма записи математических и логических выражений,
в которой операнды расположены перед знаками операций.
"""

def func(a):
    stack = []
    for i in range(len(a)):
        if a[i] == "+":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) + int(y))
        elif a[i] == "*":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(x) * int(y))
        elif a[i] == "-":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y) - int(x))
        elif a[i] == "/":
            x = stack.pop()
            y = stack.pop()
            stack.append(int(y) / int(x))
        else:
            stack.append(a[i])
    if len(stack) != 1:
        return False
    else:
        return stack[0]


a = input().split()
print(func(a))
