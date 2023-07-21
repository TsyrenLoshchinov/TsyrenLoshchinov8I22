a = str(input("введите строку: "))
p = dict.fromkeys(a)
for i in a:
    if i in "уеэоаыяию":
        p[i] = "True"
    elif i in "цкнгшщзхъждлрпвфчсмтьб":
        p[i] = "False"
    else:
        del p[i]
print(p)
