n = int(input())
if n != 0:
    m = int(input())

    s = 0

    while m != 0:
        if n % 2 != 0:
            s += m
        n = m
        m = int(input())

    if s != 0:
        print(s)
    else:
        print("-1")


else:
    print("-1")

