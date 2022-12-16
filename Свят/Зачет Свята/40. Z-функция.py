"""
Проще говоря Z-функция это префикс функция, но "наоборот". Ведь мы находим z[i] от которого суффикс
ищется вправо, а не влево. Значение z[0] можно ставить любым, но лучше 0.

         z[i] - длина максимальной строчки, которая начинатся в i позиции и равно префиксу такой же длины
           |       S[0...n-1]==S[i....i+n-1]
S = [xxx   xxx   ]
     0     i
"""

"""
Наивное вычисление
"""


def z1(s):
    z = [0] * len(s)
    for i in range(1, len(s)):
        z[i] = 0
        while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
            z[i] += 1
    return z


print(z1(list(input())))

"""
Временная сложность алгоритма - O(n**2)
"""

def z2(s):
    z = [0] * len(s)
    l=0
    for i in range(1, len(s)):
        z[i] = min(z[i-l],l+z[l]-1)
        z[i]=max(z[i],0)
        while i + z[i] < len(s) and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i+z[i]>l+z[l]:
          l=i
    return z


print(z2(list(input())))
