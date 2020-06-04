# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Решил быстрой сортировкой
import random

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)

SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 50
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE*2 + 1)]
quick_sort(arr)
print(arr)
print(f'медияной является число {arr[len(arr)//2]}')