def fun():
    b = 0
    c = int(input())

    for i in range(n):
        if li[i] == c:
            b = b + 1
    print(b)

li = []
n =int(input())
for i in range(n):
    a = int(input())
    li.append(a)
print(li)
fun()