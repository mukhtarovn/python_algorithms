# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’,‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
first = input('Введите первое число ')
second = input('Введите второе число ')
list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
if len(first) > len(second):
    first, second = second, first
second = second[::-1]
third = []
j = -1
k = 0
for i in second:
    one = list_of_numbers.index(i)
    two = list_of_numbers.index(first[j])
    third.append(list_of_numbers[(one + two + k) % 16])
    if (one + two) >= 15:
        k = 1
    else:
        k = 0
    j -= 1
    if j == -len(first)-1:
        break
diff = len(second) - len(first)

if diff:
    for i in second[-diff:]:
        third.append(list_of_numbers[(list_of_numbers.index(second[-diff]) + k) % 16])
        if list_of_numbers.index(second[-diff]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
    third.append('1')
result = third[::-1]
print(*result)

# Попытался решить через deque но не дотянул ((((
# num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
#
# n1 = []
# n2 = []
# result = []
# for i in first:
#     if i in num:
#         i = num[i]
#     n1.append(int(i))
# for i in second:
#     if i in num:
#         i = num[i]
#     n2.append(int(i))
#
# n = max(len(n1), len(n2))
# ress = deque(result)
# for i in reversed(range(n)):
#     res = n1[i]+n2[i]
#     if res > 15:
#         ress.appendleft(1)
#         res == res % 15
#     ress.append(res)
#
# print(ress)

