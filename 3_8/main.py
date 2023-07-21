a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
p = dict.fromkeys(a)
i = 1
for c in a:
    p[c] = i
    i += 1
print(p)
