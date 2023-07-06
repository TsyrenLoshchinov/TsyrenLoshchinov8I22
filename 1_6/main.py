a = str(input())
m = ""
slovo = a.split()
for i in range(len(slovo)):
    slovo[i] = slovo[i].replace(slovo[i][0],slovo[i][0].upper())
    m = m + slovo[i] + " "
print(m)


