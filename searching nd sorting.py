n = int(input())
arr =[1,2,3,4]
def fun(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return arr.index(arr[i])
        elif n not in arr:
            return -1
print(fun(arr,n))