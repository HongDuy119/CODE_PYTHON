import math
a =[1] * 1000005
a[0] = a[1] =  0
for i in range(2,int(1e6),1):
    if a[i] == 1:
        for j in range(i*2,int(1e6),i):
            a[j] = 0
def bool(d,b,c,n):
    if a[d]==0 or a[b]==0 or a[c]==0 : return False
    if(c>n): return False
    return True

for i in range(int(input())):
    n = int(input())
    dem = 0
    # print(a[8])
    for i in range(n):
        if bool(i,i+2,i+6,n) or bool(i,i+4,i+6,n):
            dem += 1
    print(dem)