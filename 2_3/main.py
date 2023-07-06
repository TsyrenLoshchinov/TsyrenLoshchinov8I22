print("Введите число: ")
sum = 0
a = int(input())
k = str(a)
d = len(k)
for i in range(d):
    sum+=pow(int(k[i]),d)
if sum == a:
    print("Это число Армстронга")
else: print("Не является числом Армстронга")