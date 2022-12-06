data = list(map(str, input().split()))

new_data = [[], []]
cnt = 0
for i in data:
    cnt = max(cnt, len(i))

for k in range(cnt):
    for i in range(len(data)):
        if len(data[i]) > k:
            new_data[int(data[i][len(data[i]) - k - 1])].append(data[i])
        else:
            new_data[0].append(data[i])

    data = new_data[0] + new_data[1]
    print(*data)
    new_data = [[], []]

