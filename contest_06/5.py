data = list(map(int, input().split()))

cnt = [0 for i in range(10)]

for i in data:
    cnt[i] += 1
    print(*cnt)


for i in range(len(cnt)):
    for _ in range(cnt[i]):
        print(i, end=" ")
