# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.
# Решил рекурсивно решить эту задачу
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=aPmPMU5d6-vtcc42iAdE#G1uYQRNEP7ipgP9LgRCkpbAbG9OIGPtf17
import random
import timeit



a = random.randint(1,100)
def my_func (user, count):
    user = int(input("Введи число "))
    if user == a or count == 10:
        print(f'загаданое число {a}')
    elif user > a:
        print('Меньше!')
        my_func (user, count=count+1)
    else:
        print ('Больше!')
        my_func (user, count=count+1)

count=1
user = 0
my_func(user, count)
print(timeit.timeit('my_func(18)'))