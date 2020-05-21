# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=mnA2kJPN5Pg51JmEBjOG#G1uYQRNEP7ipgP9LgRCkpbAbG9OIGPtf17
num = int(input('Введите число '))
m = 0
while num > 0:
    m = m * 10 + num % 10
    num //= 10
print(m)



