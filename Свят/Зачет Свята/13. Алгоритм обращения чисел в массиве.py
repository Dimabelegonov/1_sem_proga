def func(a):
    for i in range(len(a) // 2):
        a[i], a[-(i + 1)] = a[-(i + 1)], a[i]
    print(a)


func(list(input()))
