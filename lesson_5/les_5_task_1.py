"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections


def sum_tuple(numbers):
    #tuple -> sum

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Enter_san = collections.namedtuple('Enter', ['a1', 'a2', 'a3', 'a4'])

general_enter_san = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_a1 = int(input('Прибыль за 1-й квартал: '))
    profit_a2 = int(input('Прибыль за 2-й квартал: '))
    profit_a3 = int(input('Прибыль за 3-й квартал: '))
    profit_a4 = int(input('Прибыль за 4-й квартал: '))
    general_enter_san[name] = Enter_san(
        a1=profit_a1,
        a2=profit_a2,
        a3=profit_a3,
        a4=profit_a4
    )

general_profit = ()

for name, profit in general_enter_san.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    general_profit += profit

avg_profit_general = sum(general_profit) / len(general_enter_san)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_general}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in general_enter_san.items():
    if sum(profit) > avg_profit_general:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in general_enter_san.items():
    if sum(profit) < avg_profit_general:
        print(f'{name} - {sum(profit)}')