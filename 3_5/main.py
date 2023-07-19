def s(a):
    k = 0
    for i in range(2, a // 2 +1 ):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return a
    else:
        None
a = [i for i in range(1,100) if s(i) != None]
print(a)