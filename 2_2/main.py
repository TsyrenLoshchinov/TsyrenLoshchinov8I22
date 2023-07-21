tv_shows = ["Мир наизнанку", "Орел и решка", "Однажды в России", "Кондитер"]
for show in tv_shows:
    print(show)
print("Введите навзвание телепередачи: ")
new_show = str(input())
print("Введите позицию: ")
position = int(input())
tv_shows.insert(position - 1, new_show)
for show in tv_shows:
    print(show)
