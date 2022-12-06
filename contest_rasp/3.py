n = int(input())
data = []
data_ = []
for i in range(n):
    a = int(input())
    if a >= 0:
        data.append(a)
    else:
        data_.append(a)

data.sort()
data_.sort(key=lambda x: abs(x))
data += data_
print(*data)
