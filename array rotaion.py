def checkRotate(arr):
    m = min(arr)
    list = arr.index(m)
    print(list)


n = int(input())
arr = [int(x) for x in input().split()[:n]]
checkRotate(arr)