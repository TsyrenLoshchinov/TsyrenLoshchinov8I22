a = str(input())
m = ""
slovo = a.split()
for i in range(len(slovo)):
    slovo[i] = slovo[i].swapcase()
    m = m + slovo[i] + " "
print(m)
