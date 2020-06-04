# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random
from timeit import timeit


def bubbles_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return f'Сортировка обычным пузырьком {arr[::-1]}'

def bubble_sort_modyf(arr):
    for i in range(len(array) - 1):
        flag = True
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = False

        if flag == True:
            break
    return f'Модифицированый алгоритм сортировки пузырьком {arr[::-1]}'
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный массив {array}')
print(bubbles_sort(array))
print(bubble_sort_modyf(array))

# print(timeit.timeit('bubbles_sort(array)', number=100, globals=globals))
# print(timeit.timeit('bubble_sort_modyf(array)', number=100, globals=globals))

