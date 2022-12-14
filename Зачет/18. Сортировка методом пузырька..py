"""
Сортировка пузырьком - это метод сортировки массивов и списков путем
последовательного сравнения и обмена соседних элементов, если предшествующий
оказывается больше последующего.
"""

data = list(map(int, input().split()))
for i in range(len(data) - 1):
    print(data)
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)

"Временная сложность алгоритма - O(n**2)"
