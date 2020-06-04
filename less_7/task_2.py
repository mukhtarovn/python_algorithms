# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
    def merge(first, second):
        res = []
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                res.append(first[i])
                i += 1
            else:
                res.append(second[j])
                j += 1
        res.extend(first[i:] if i < len(first) else second[j:])
        return res
    def div_half(list):
        if len(list) == 1:
            return list
        elif len(list) == 2:
            return list if list[0] <= list[1] else list[::-1]
        else:
            return merge(div_half(list[:len(list)//2]), div_half(list[len(list)//2:]))
    return div_half(arr)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Массив:{array}')
print(f'Отсортированный: {merge_sort(array)}')
