#4. Определить, какое число в массиве встречается чаще всего.

import random

r = [random.randint(0, 20) for _ in range(20)]
print(f'Массив: {r}')

num = 0
for i in r:
    if r.count(num) < r.count(i):
        num = r.index(i)

if r.count(num) > 1:
    print(r.count(num), 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')