#  Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
#  Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=mO-cpp9L30hnZ1-snd5J#G1uYQRNEP7ipgP9LgRCkpbAbG9OIGPtf17

lot = int (input("Сколько будет чисел? "))
num = int (input("Какую цифру считать? "))
count = 0
for i in range(1, lot + 1):
    m = int(input(f'Число {i}: '))
    while m > 0:
        if m % 10 == num:
            count += 1
        m = m // 10

print(f'Цифра {num} была введена{count} раз(а)')

