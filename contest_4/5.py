def get_(n):
    t = int(n ** (1 / 3)) + 2
    for b in range(t):
        for a in range(t):
            if a ** 3 + b ** 3 == n:
                return sorted([a, b])
            elif a ** 3 + b ** 3 > n:
                break

    return ["impossible"]


k = int(input())

"""if int(k ** (1 / 3)) == round(k ** (1 / 3)):
    print(0, int(k ** (1 / 3)))
else:"""
print(* get_(k))

