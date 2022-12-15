def func(a, s):
    for i in range(s):
        a.append(a.pop(0))
    print(a)


func(list(input()), int(input()), )
