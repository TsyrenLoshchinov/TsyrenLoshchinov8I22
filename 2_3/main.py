print("Введите число: ")
s = 0
a = int(input())
k = str(a)
d = len(k)
for i in range(d):
    s += pow(int(k[i]), d)
if s == a:
    print("Это число Армстронга")
else:
    print("Не является числом Армстронга")
