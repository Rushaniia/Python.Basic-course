"""Тесты выполнены на 64-разрядной Win 10 версии 1803
Python 3.9.0"""

import sys

def memory_size(x, level=0):
    size_p = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_p}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                memory_size(key, level + 1)
                size_p = size_p + sys.getsizeof(key)
                memory_size(value, level + 1)
                size_p = size_p + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                memory_size(item, level + 1)
                size_p = size_p + sys.getsizeof(item)
    return size_p

"""Задача 3, урок 2: Сформировать из введенного числа обратное по порядку
входящих в него цифр и вывести на экран"""

#способ 1
new_number = ''

number = input('Введите число: ')
count = len(number)
k = range(count)

for i in k:
    new_number = new_number + str(int(number) % 10)
    number = int(number) // 10
print(new_number)

sum_member1 = memory_size(new_number) + memory_size(number) + memory_size(count) + memory_size(k)
print('В программе задействовано байт памяти: {}'.format(sum_member1))

# Затраты памяти программы:  163
# Переменная:  201813


#способ 2
number = input('Введите число: ')
new_number = number[::-1]
print(new_number)

sum_member2 = memory_size(new_number) + memory_size(number)
print('В программе задействовано байт памяти: {}'.format(sum_member2))


# Затраты памяти программы:  62
# Переменная:  201813


# способ 3
x = input('Введите число ')
number = int(x)
new_number = 0
while number > 0:
    new_number = new_number * 10 + number % 10
    number = number//10
print(new_number)

sum_member3 = memory_size(new_number) + memory_size(x)
print(f'В программе задействовано байт памяти: {sum_member3}')


# Затраты памяти программы:  47
# Переменные:  201813

