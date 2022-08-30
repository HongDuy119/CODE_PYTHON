import math
from tkinter import N


n = int(input())
a = list(map(int,input().split()))
minN = 10**18
index = -1
for i in range(n-1,-1,-1):
    sum = 0
    for j in range(n):
        sum = sum+abs(a[i]-a[j])
    if sum<=minN:
        minN = sum
        index = a[i]
print(minN,index)