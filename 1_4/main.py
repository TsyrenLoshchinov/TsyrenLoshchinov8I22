print("Введите число от 10 дот 20: ")
a = int(input())
while (a < 10) or (a > 20):
    if a < 10:
        print("Число меньше требуемого диапозона")
    if a > 20:
        print("Число больше требуемого диапозона")
    print("Введите число от 10 дот 20: ")
    a = int(input())
print("Спасибо")
