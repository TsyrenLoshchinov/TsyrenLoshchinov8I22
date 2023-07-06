tvshows = ["Мир наизнанку","Орел и решка","Однажды в России","Кондитер"]
for show in tvshows:
    print(show)
print("Введите навзвание телепередачи: ")
newshow = str(input())
print("Введите позицию: ")
position = int(input())
tvshows.insert(position-1,newshow)
for show in tvshows:
    print(show)