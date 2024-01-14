def fun(n,a,b,c):
    if n == 1 :
        print("move disk 1 from", a , "to", c)
        return
    fun(n-1 ,a ,c ,b)
    print("move disk", n ,"the from", a, "to", c)
    fun(n-1,b,a,c)

