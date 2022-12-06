a, b = map(int, input().split())

if a > b * 9 or a < b:
    print("impossible")
else:
    _s = 0
    ans = ""
    while _s < a:

        t = a - _s

        if t // 9 == b:
            ans += "9"
            _s += 9
            b -= 1
        elif (t - 1) <= (b - 1) * 9:
            ans += "1"
            _s += 1
            b -= 1
        else:
            _s += t % 9
            ans += str(t % 9)
            b -= 1

    print(ans)
