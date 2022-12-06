def get_fb(a):
    global fb

    if a == n:
        print(fb[a - 1] + fb[a - 2])
        return
    else:
        fb[a] = fb[a - 1] + fb[a - 2]
        get_fb(a + 1)


n = int(input())
fb = [0] * (n + 3)
fb[0] = fb[1] = 1
if n > 1:
    get_fb(2)
else:
    print(1)

