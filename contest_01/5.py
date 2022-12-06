a = int(input())
s = input()
t = 0

if s == "monkey":
    t = int(a / 90)
    t = 1 if t == 0 else t
elif s == "parrot":
    t = int(a / 10)
    t = 1 if t == 0 else t
elif s == "elephant":
    t = int(a / 300)
    t = 1 if t == 0 else t

print(t)
