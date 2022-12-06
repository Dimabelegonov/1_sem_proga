e = 3
N = 187
d = 107


data = list(map(int, input().split()))


for y in data:
    x = (y ** d) % N
    print(x, end=" ")

