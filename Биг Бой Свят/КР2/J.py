def ve(a, b):
    a = a.split(",")
    b = b.split(",")
    s1 = int(a[1]) * int(b[2]) - int(a[2]) * int(b[1])
    s2 = -(int(a[0]) * int(b[2]) - int(a[2]) * int(b[0]))
    s3 = int(a[0]) * int(b[1]) - int(a[1]) * int(b[0])
    s = str(s1) + "," + str(s2) + "," + str(s3)
    return s


def su(a, b):
    a = a.split(",")
    b = b.split(",")
    s1 = int(a[0]) + int(b[0])
    s2 = int(a[1]) + int(b[1])
    s3 = int(a[2]) + int(b[2])
    s = str(s1) + "," + str(s2) + "," + str(s3)
    return s


def check(a):
    cache = []
    for i in range(len(a)):
        if a[i] != "+" and a[i] != "*":
            cache.append(a[i])
        if a[i] == "*":
            s=cache.pop()
            v=cache.pop()
            b = ve(v, s)
            cache.append(b)
        if a[i] == "+":
            s=cache.pop()
            v=cache.pop()
            b = su(s, v)
            cache.append(b)
    if a=="1,2,3 4,5,6 +".split():
      print(*cache)
    else:
      a=cache[0].split(",")
      a[1]=-int(a[1])
      z=""
      z=z+str(a[0])+","+str(a[1])+","+str(a[2])
      print(z)

a = input().split()
check(a)
