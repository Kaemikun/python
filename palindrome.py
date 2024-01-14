n = int(input())
# taking n as a input
## write your code !!
def fun(n):
    temp = n
    a = 0
    while n !=0:
        b = n % 10
        a = a * 10 + b
        n = n // 10


    if a == temp :
        return True
    else :
        return False

if fun(n):
    print("true")
else:
    print("false")
