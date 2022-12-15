def func(a, h):
    if len(a) == 4:
        print(a)
        return

    for x in range(len(h)):
        func(a + h[x], h[:x] + h[x + 1:])


func("", "abcdefgh")
