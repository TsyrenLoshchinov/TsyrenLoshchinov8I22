print("Сколько километров хотите проехать на автомобиле?")
a = float(input())
print("Сколько литров топлива расходует автомобиль на 100 километров?")
b = float(input())
print("Сколько литров топлива в вашем баке?")
c = float(input())
r = c/b
if r*100>=a:
    print("Проедите")
else:
    print("Бензина не хватит")
