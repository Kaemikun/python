def fun(li):
    a = 0
    b = 0
    for i in range(n):
        if li[i] > b:
            a = b
            b = li[i]

    print(a , b)
li = []
n = int(input())
for i in range(n):
    d = int(input())
    li.append(d)
fun(li)