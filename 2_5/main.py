import random
print("Орел(0) или Решка(1)?")
lose = 0
win = 0
while lose < 3:
    a = int(input())
    k = random.randint(0, 1)
    if a == k:
        win += 1
        print("Угадал(а)")
    elif (a != k) and (a == 1 or a == 0):
        lose += 1
        print("Не угадал(а)")
    else:
        break
print(win, " раз угадал(а) и ", lose, "раз не угадал(а)")
