# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


def without_eratosthenes(user):
    res = [2]
    number = 3
    while len(res) < user:
        flag = True
        for j in res.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            res.append(number)
        number += 1
    return f'{res[-1]} - {user} по счету простое число'


def eratosthenes(user):
    n = 100  # решил задать длину списка
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return f'{b[user - 1]} - {user} по счету простое число'


user_number = int(input('Введите номер по счету простого числа: '))

print('без использования алгоритма «Решето Эратосфена»')
print(without_eratosthenes(user_number))

print('c использованием алгоритма «Решето Эратосфена»')
print(eratosthenes(user_number))
