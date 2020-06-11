user = str (input ("Введите строку S: "))

print(f'Строка {user} имеет длину {len(user)}сиволов.')
subs_set = set()
for i in range (len(user)):
    for j in range (len (user) - 1 if i == 0 else len(user), i, -1)
subs_set.add (hash(user[i:j]))
        print(user[i:j], i, j)
        # subs_dict[S[i:j]] = hash(S[i:j])

# print(len(list(subs_dict.keys())), list(subs_dict.keys()))
print ("Количество различных подстрок в этой строке:", len (subs_set))