n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

s = int(input())

data.sort(key=lambda x: x[0])

t = 0
i = 0
answer = [0, 0]
while t < s:
    if t + data[i][0] <= s:
        t += data[i][0]
        answer[0] += 1
        answer[1] += data[i][1]
        i += 1
    else:
        break

print(*answer)
