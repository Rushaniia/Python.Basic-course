'''
Проанализировать скорость и сложность одного любого алгоритма из
разработанных в рамках домашнего задания первых трех уроков.
'''

'''les_3_task_3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import timeit
import cProfile

# Вариант №1

import random

r = [random.randint(0, 1000000000000000000000000000000000000000000000) for _ in range(10)]
# print(f'Массив {r}')
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

print(
    timeit.timeit('r', number=100, globals=globals()),  #1.180000000000625e-05
    timeit.timeit('r', number=100, globals=globals()),   #6.900000000004125e-06
    timeit.timeit('r', number=100, globals=globals()),   #4.6.699999999998374e-06
    sep='\n'
    )

cProfile.run('r')
# 3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вариант №2

import random
a = [random.randint(0, 99) for _ in range(10)]
# print(f'Массив {a}')
imax, imin = a.index(max(a)), a.index(min(a))
a[imax], a[imin] = a[imin], a[imax]
# print (f'Новый массив: {a}')

print(
    timeit.timeit('a', number=100, globals=globals()),  #6.3000000000007494e-06
    timeit.timeit('a', number=100, globals=globals()),   #3.900000000001125e-06
    timeit.timeit('a', number=100, globals=globals()),   #3.900000000001125e-06
    sep='\n'
    )
cProfile.run('a')
# 3 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант №3

import random


def get_array(arr, arr_1):
    array = [random.randint(arr, arr_1) for _ in range(10)]
#    print(f'Массив {array}')
    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array
#    print(f'Новый массив: {array}')

print(f'Новый массив: {get_array(0, 99)}')
print(
    timeit.timeit('get_array(0, 1000000)', number=100, globals=globals()),  #0.0015092000000000022
    timeit.timeit('get_array(0, 1000000000)', number=100, globals=globals()),   #0.0015469999999999998
    timeit.timeit('get_array(0, 10000000000000)', number=100, globals=globals()),   #0.0017177000000000026
    sep='\n'
    )


cProfile.run('get_array(0, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)')

# 58 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:43(get_array)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:44(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

