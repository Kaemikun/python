l1 = [0,1,1,0,0,1,0]
b = 0
for i in range(len(l1)):
    if l1[i] == 0:
        temp = l1[b]
        l1[b] = l1[i]
        l1[i] = temp
        b +=1


print(l1)