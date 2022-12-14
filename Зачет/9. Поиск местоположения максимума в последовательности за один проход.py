def max_search():                   # Программа ищет максимальный элемент в последовательности за один проход
    x = -1                          # Текущий считываемый элемент
    max_element = float('-inf')     # Текущий максимальный элемент
    n = 0                           # Колво считанных элементов, не равных данному
    s = 0                           # Актуальное положение максимума
    while x != 0:                   # Считываение идет до момента, пока x не будет равен 0
        n += 1
        x = int(input())
        if x > max_element:
            max_element = x
            s = n
    print(s)                        # Программа выведет первое вхождение максимума


max_search()
