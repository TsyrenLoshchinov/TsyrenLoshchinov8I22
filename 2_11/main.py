a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
sum = 0
for i in range(a,b+1):
    sum+=i
print("Сумма чисел между a и b включительно: ", sum)