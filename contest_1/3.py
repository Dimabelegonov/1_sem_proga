a = int(input())
b = int(input())
c = int(input())

a, b, c = sorted([a, b, c], reverse=True)

if a + b > c:
    if a + c > b:
        if c + b > a:
            if a ** 2 == b ** 2 + c ** 2:
                print("right")
            else:
                if (b ** 2 + c ** 2 - a ** 2) > 0:
                    print("acute")
                else:
                    print("obtuse")
        else:
            print("impossible")
    else:
        print("impossible")
else:
    print("impossible")
