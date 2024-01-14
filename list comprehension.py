def fun(n):
    a = 0
    for i in str(n):
        a += int(i)
    return a
l = [123,145,254,102]
l2 = [fun(i) for i in l]
print(l2)
