#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме
# цифр. Вывести на экран это число и сумму его цифр.


def sum_numbers(number):
    if number < 10:
        return number
    return number % 10 + sum_numbers(number // 10)


number = int(input('Введите натуральное число: '))
max_number = 0
max_sum = 0

while number != 0:
    m = number
    s = sum_numbers(number)
    if s > max_sum:
        max_sum = s
        max_number = m
    number = int(input('Введите натуральное число: '))
print('Число',max_number,'имеет максимальную сумму цифр:', max_sum)