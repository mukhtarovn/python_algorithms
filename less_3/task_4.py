# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве
# задача №5 из урока 3

import random
import timeit
import cProfile

SIZE = 10000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(*array)


def min_numb_1(n):
    min_num = MIN_ITEM
    for i in n:
        if i < 0:
            if i > min_num:
                min_num = i
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
    return f'позиция {pos + 1}, число {m}'


print(min_numb_1(array))

print(min_numb_2(array))

print(min_numb_3(array))

print(timeit.timeit('min_numb_1(array)', number=100, globals=globals()))  # 0.036446320000000004
print(timeit.timeit('min_numb_2(array)', number=100, globals=globals()))  # 0.177791082
print(timeit.timeit('min_numb_3(array)', number=100, globals=globals()))  # 0.059751316
cProfile.run('min_numb_1(array)')
cProfile.run('min_numb_2(array)')
cProfile.run('min_numb_3(array)')
'''Функция 1 работает быстрее всех. Мне кажется, что он представляет логарифмическую сложность O(log n)
   Функция 2 представляет квадратичную сложность O(n2)
   Функция 3 представляет линейную сложность O(n)
'''