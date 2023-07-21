a = int(input("Введите число: "))
print((lambda k: print("Четное") if a % 2 == 0 else print("Нечетное"))(a))
