import math
a =[1] * 1000005
a[0] = a[1] =  0
for i in range(2,int(1e6),1):
    if a[i] == 1:
        for j in range(i*2,int(1e6),i):
            a[j] = 0
array = []
for i in range(2,int(1e6),1):
    if a[i] == 1: array.append(i)
[n,x] = input().split()
n,x = int(n),int(x)
print(x,end=' ')
for i in range(n):
    x += array[i]
    print(x,end = " ")