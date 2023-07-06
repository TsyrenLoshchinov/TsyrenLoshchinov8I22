a = int(input("Введите натуральное число: "))
k = str(a)
m = 0
y = 0
x = 0
for i in range(len(k)):
    if int(k[i]) > m:
        m = int(k[i])
        y = i+1
x = len(k)-y+1
print(m," - максимальная цифра")
print(y," - позиция от начала")
print(x," - позиция с конца")