# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

n = int(input('Сколько предприятий будет? '))
s = 0

res = defaultdict(list)
for i in range(n):
    firm = input(f'Введите название {i+1} -й фирмы: ')
    for j in range(4):
        profit = int(input(f'Введите прибыль {firm} за {j+1} -й квартал: '))
        res[firm].append(profit)
        s += profit
avg = s/n
print(f'Средняя прибыль компаний {avg}')
print(f'Общая прибыль компаний {s}')
for i in res:
    if sum(res[i]) > avg:
        print(f'Прибыль {i} выше среднего')
    else:
        print(f'Прибыль {i} ниже среднего')
