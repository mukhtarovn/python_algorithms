# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Ссылка на блок-схему
# https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=hj45UPNGrU8KSZuhcKLE#G1CC1TMSBnVCWUhqBjExSD1V_TGhG3Ye44

n = int(input('Номер буквы в алфавите: '))
n = ord('a') + n - 1
res = chr(n)
print(f'Это буква {res}')
