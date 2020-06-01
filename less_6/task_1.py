# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
# задача №5 из урока 3

# Python 3.8.0
# Mac OS 64

import random
import sys


SIZE = 1000
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)


def min_numb_1(n):
    min_num = MIN_ITEM
    for i in n:
        if i < 0:
            if i > min_num:
                min_num = i
    size = 0
    size += sys.getsizeof(n)
    size += sys.getsizeof(min_num)
    size += sys.getsizeof(i)
    size += sys.getsizeof(size)
    print(f'Переменные функции 1 заниямают {size}')
    return f'позиция {n.index (min_num) + 1}, число {min_num}'


def min_numb_2(n):
    i = 0
    index = -1
    while i < SIZE:
        if n[i] < 0 and index == -1:
            index = i
        elif 0 > n[i] > n[index]:
            index = i
        i += 1
    size = 0
    size += sys.getsizeof(i)
    size += sys.getsizeof(index)
    size += sys.getsizeof(n)
    size += sys.getsizeof(size)
    print(f'Переменные функции 2 заниямают {size}')
    return f'позиция {index + 1}, число {n[index]}'



def min_numb_3(n):
    arr = []
    for i in n:
        if i < 0:
            arr.append(i)
    m = max(arr)
    pos = None
    for j in enumerate(n):
        if j[1] == m:
            pos = j[0]
            break
    size = 0
    size += sys.getsizeof(arr)
    size += sys.getsizeof(i)
    size += sys.getsizeof(j)
    size += sys.getsizeof(pos)
    size += sys.getsizeof(m)
    size += sys.getsizeof(n)
    size += sys.getsizeof(size)
    print(f'Переменные функции 3 заниямают {size}')
    return f'позиция {pos + 1}, число {m}'


print(min_numb_1(array))
print(min_numb_2(array))
print(min_numb_3(array))


''' Очевидно, что функция 3 использует память больше остальных'''

