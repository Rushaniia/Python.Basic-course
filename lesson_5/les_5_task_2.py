"""Написать программу сложения двух положительных целых
шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь
ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’]"""

from collections import deque


def sum_hex(x, y):
    HEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    w = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = HEX[x.pop()] + HEX[y.pop()] + w

        else:
            res = HEX[x.pop()] + w

        w = 0

        if res < 16:
            result.appendleft(HEX[res])

        else:
            result.appendleft(HEX[res - 16])
            w = 1

    if w:
        result.appendleft('1')

    return list(result)


z = list(input('Введите 1-е шестнадцатиричное число: ').upper())
c = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(*z, '+', *c, '=', *sum_hex(z, c))