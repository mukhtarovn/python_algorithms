# Вводятся три разных числа. Найти, какое из них является средним.
# Ссылка на блок-схему
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1#G1CC1TMSBnVCWUhqBjExSD1V_TGhG3Ye44

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

if b < a < c or c < a < b:
    print(f'Среднее: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее: {b}')
else:
    print(f'Среднее: {c}')
