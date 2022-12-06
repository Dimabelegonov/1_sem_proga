s = input()
data = []
a = ""
for i in range(len(s)):
    if s[i] in "1234567890":
        a += s[i]
    else:
        if len(a) != 0:
            data.append(int(a))
            a = ""

if len(a) != 0:
    data.append(int(a))
    a = ""

pr = 1
for i in data:
    pr *= i

print(pr)
