"""
Сортировка вставками очень похожа на сортировку пузырьком, однако между ними различие есть,
и не стоит их путать. На каждой итерации алгоритма будет выполняться сортировка только первых
i элементов. Пусть уже первые i−1 элементов отсортированы, и мы добавили в конец новый
элемент. Этот новый элемент нужно передвинуть на правильное место, чтобы снова получить отсортированный массив.
Будем просто пытаться обменивать его местами с соседом слева, если этот сосед больше нового элемента.
Эта сортировка – устойчивая, время работы – O(n**2).
"""


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


print(insertion_sort([5, 2, 3, 4, 1]))
