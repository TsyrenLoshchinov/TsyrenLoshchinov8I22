print("Введите число")
a = int(input())
sum=0
while a<0:
    sum+=a
    print("Введите число")
    a = int(input())
print(sum)