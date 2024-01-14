n =int(input())
for i in range(n):
    for j in range(i+1):
        if i == 0 or i == n-1 or j == 0 or j == i :
            print("*",end = " ")
        else :
            print(" ",end = " ")
    print()