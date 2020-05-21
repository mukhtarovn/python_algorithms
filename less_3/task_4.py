# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)

min_num = MIN_ITEM
for i in array:
    if i < 0:
        if i > min_num:
            min_num = i

print(f'Максимальный отрицательный элемент в массиве: {min_num}\n'
      f'Позиция в массиве: {array.index(min_num)}')

