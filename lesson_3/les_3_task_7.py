#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random

r = [random.randint(0, 99) for _ in range(15)]
print(f'Массив {r}')

min1 = 0
min2 = 1

for i in r:
    if r[min1] > i:
        min2 = min1
        min1 = r.index(i)
    elif r[min2] > i:
        min2 = r.index(i)

print(f'Наименьший элемент 1: {r[min1]}')
print(f'Наименьший элемент 2: {r[min2]}')