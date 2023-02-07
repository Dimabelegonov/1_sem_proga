def func(a):
    arr = []
    k = 2
    while a != 1:
        if a % k == 0:
            arr.append(k)
            a = a // k
        else:
            k = k + 1
    for i in arr:
        print(i)


a = int(input())
func(a)
