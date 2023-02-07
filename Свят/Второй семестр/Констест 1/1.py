def func(a):
    s = 0
    while a != 0:
        s = s + a % 10
        a = a // 10
    return s


a = int(input())
print(func(a))
