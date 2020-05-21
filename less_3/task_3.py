# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_arr = []
while len(array) > SIZE-2:
    min_num = MAX_ITEM
    for i in array:
        if i < min_num:
            min_num = i
    min_arr.append(min_num)
    array.remove(min_num)

print(f'Два наименших элемента списка: {min_arr}')



