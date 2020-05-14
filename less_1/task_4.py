# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
# Ссылка на блок-схему:
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-2Y5ssmW6y_uvMR_2e1-#G1CC1TMSBnVCWUhqBjExSD1V_TGhG3Ye44


a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))

a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'Позиции: {a}, {b}')
print(f'Между буквами символов: {(b-a)-1}')