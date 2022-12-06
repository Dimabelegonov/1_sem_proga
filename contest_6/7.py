def get_s(x):
    return sum(list(map(int, x)))


n = int(input())
data = []
for _ in range(n):
    flag = False
    a = input()
    for i in range(len(data)):
        if get_s(a) < get_s(data[i]):
            data = data[:i] + [a] + data[i:]
            flag = True
            break
        elif get_s(a) == get_s(data[i]):
            if int(a) < int(data[i]):
                data = data[:i] + [a] + data[i:]
                flag = True
                break

    if not flag:
        data.append(a)


for i in data:
    print(i)
