# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=OMZQ-isXMUxkyaAR2x6k#G1uYQRNEP7ipgP9LgRCkpbAbG9OIGPtf17

user = int(input('Введите число '))
even = 0
odd = 0
while user != 0:
    if user % 2 == 0:
        even +=1
    else:
        odd +=1
    user //= 10
print(f'четных чисел {even}, нечетныx чисел {odd}')

