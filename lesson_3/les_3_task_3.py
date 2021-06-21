# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Массив {r}')
min1 = r[0]
max1 = r[0]

for i in r:
    if i < min1:
        min1 = i
    elif i > max1:
        max1 = i
min_index = r.index(min1)
max_index = r.index(max1)
r[min_index], r[max_index] = r[max_index], r[min_index]
print (f'максимальный элемент {max1} и минимальный элемент {min1}')
print (f'Новый массив: {r}')