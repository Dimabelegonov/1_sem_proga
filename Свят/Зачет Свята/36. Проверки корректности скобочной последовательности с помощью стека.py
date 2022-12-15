def check(a):
    stack = []
    for ch in a:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if len(stack) == 0 or stack.pop() + ch not in "(){}[]":
                return False
    return len(stack) == 0


print(check(input()))
