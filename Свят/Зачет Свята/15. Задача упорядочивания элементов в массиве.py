def func(a):
    for i in range(len(a) - 1):
        if a[i + 1] < a[i]:
            return False
    return True


print(func(list(map(int, input().split()))))
