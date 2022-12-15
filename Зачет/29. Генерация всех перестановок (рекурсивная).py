def gen(s, letters):
    if len(s) == 4:
        print(s)
        return

    for x in range(len(letters)):
        gen(s + letters[x], letters[:x] + letters[x + 1:])


gen("", "abcdef")
