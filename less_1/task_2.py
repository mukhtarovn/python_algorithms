# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь
# Ссылка на блок схему:
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=-f9dKNc2gsp68ILxeg_n#G1CC1TMSBnVCWUhqBjExSD1V_TGhG3Ye44

n = int(input('Введите трехзначное число '))

a = n // 100
b = n % 100 // 10
c = n % 10

res_1 = a + b + c
res_2 = a * b * c

print(f'Сумма чисел {res_1}')
print(f'Произведение чисел {res_2}')


