def vecsum(v1: str, v2: str):
    v1 = list(map(int, v1.split(",")))
    v2 = list(map(int, v2.split(",")))
    v3 = [0] * 3

    for i in range(3):
        v3[i] = v1[i] + v2[i]
    return ",".join(map(str, v3))


def vec(v1: str, v2: str):
    v1 = list(map(int, v1.split(",")))
    v2 = list(map(int, v2.split(",")))
    v3 = [v1[1] * v2[2] - v1[2] * v2[1], v1[0] * v2[2] - v1[2] * v2[0], v1[0] * v2[1] - v1[1] * v2[0]]
    return ','.join(map(str, v3))


input_vector = input().split()
mass = []
for i in input_vector:
    if i in ["*", "+"]:
        v1 = mass.pop()
        v2 = mass.pop()
        if i == "+":
            mass.append(vecsum(v1, v2))
        else:
            mass.append(vec(v2, v1))
    else:
        mass.append(i)
print(",".join(mass))
