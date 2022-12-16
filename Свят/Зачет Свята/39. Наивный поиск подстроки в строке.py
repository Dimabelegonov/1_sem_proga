def func(a, b):
    for i in range(len(a) - len(b) + 1):

        for j in range(len(b)):
            if a[i + j] != b[j]:
                break
        else:
            return True
    return False


a = input()
b = input()
print(func(a, b))
