data = list(map(float, input().split()))
n = abs(data[0] - data[1])
st = n * data[-1]
k = abs(data[0] - data[2])
el = k * data[3]
el += n * data[3]
el += data[-2] * 3
if el < st:
    print("elevator")
else:
    print("stairs")
