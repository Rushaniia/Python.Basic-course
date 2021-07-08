# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание:
# задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


m = 5
size = 2 * m + 1
lst_1 = [random.randint(1, 70) for i in range(size)]

print(f'Исходный НЕотсортированный список:\n {lst_1}\n')


def median(lst):
    # нахождение медианы для четного кол-ва элементов
    if len(lst) % 2 == 0:
        center = []

        for i in lst:
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == b * 2 + 2 or len(lst) == b * 2:
                center.append(i)
        return sum(center) / 2

    # нахождение медианы для НЕ четного кол-ва элементов
    else:
        for i in lst:
            num = i
            b = 0

            for j in lst:

                if i < j:
                    b += 1

            if len(lst) == 2 * b + 1:
                return num


print(f'Медиана неотсортированного списка: {median(lst_1)}\n')

print(f'Отсортированный список: \n{sorted(lst_1)}')