# n = int(input())
# i = 1
# while i <=n:
#     space= 1
#     while space <= n-i :
#         print(" ",end ="")
#         space = space + 1
#     j = 1
#     while j <= i :
#         print(n-i+j,end = "")
#         j = j +1
#     print()
#     i = i+1
# n = int(input())
# m = n//2 +1
# for i in range(m):
#     print(" "*(n-i-1) + "*"*(i))
# for i in range(m):
#     print(" "*(i) + "*"*(n-i-1) )
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print(j+1,end = "")
#     print()
# n =int(input())
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print(n,end = "")
#         elif i == 1 or i == n-2 or j == 1 or j == n-2:
#             print(n-1,end = "")
#         else:
#             print(n-2,end = "")
#     print()
# n = int(input())
# m = n//2 +1
# for i in range(m-1):
#     for j in range(m-i-1):
#         print(" ",end = "")
#     for j in range(i):
#         print("*",end = "")
#     for j in range(i+1):
#         print("*",end = "")
#     print()
# for i in range(m):
#     for j in range(i):
#         print(" ",end = "")
#     for j in range(m-i):
#         print("*",end = "")
#     for j in range(m-i-1):
#         print("*",end = "")
#     print()
# n = int(input())
# for i in range(n):
#     for j in range(i):
#         if i == 0 or i == n-1 or j == 0 or j == i-1:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()