def F(a, b, c, d):
    if a > 8 or b > 8 or (c - 1 == a and d - 2 == b) or (c + 1 == a and d - 2 == b) or (c + 1 == a and d + 2 == b) or (
            c - 1 == a and d + 2 == b) or (c + 2 == a and d - 1 == b) or (c - 2 == a and d - 1 == b) or (
            c + 2 == a and d + 1 == b) or (c - 2 == a and d + 1 == b) or (a == c and b == d):
        return 0
    if a == 8 and b == 8:
        return 1
    return F(a + 1, b, c, d) + F(a, b + 1, c, d) + F(a + 1, b + 1, c, d)


a = list(input())
b = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(len(b)):
    if a[0] == b[i]:
        a[0] = i
        break
print(F(1, 1, int(a[0]), int(a[1])))
