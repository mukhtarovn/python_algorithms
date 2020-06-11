#Определение количества различных подстрок с использованием хеш-функции.
#Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

user = str(input("Введите строку: "))

print(f'Строка {user} имеет длину {len(user)} сиволов.')

subs_set = set()
for i in range(len(user)):
    for j in range(len(user) - 1 if i == 0 else len(user), i, -1):
        subs_set.add(hash(user[i:j]))

print(f'Количество подстрок в этой строке:{len(subs_set)}')
