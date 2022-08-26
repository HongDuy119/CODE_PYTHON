import math
a =[1] * 1000005
a[0] = a[1] =  0
b = []
for i in range(2,int(1e6),1):
    if a[i] == 1:
        b.append(i)
        for j in range(i*2,int(1e6),i):
            a[j] = 0
n = int(input())
dem = 0
if math.pow(2,8)<n:
    dem += 1
if math.pow(3,8)<n:
    dem += 1
if math.pow(5,8)<n:
    dem += 1
if math.pow(7,8)<n:
    dem += 1       
if math.pow(11,8)<n:
    dem += 1 
if math.pow(13,8)<n:
    dem += 1
for i in range(0,9300,1):
    if pow(b[i],2)*pow(b[i+1],2)>=n:break
    for j in range(i+1,9300 ,1):
        if math.pow(b[i],2)*math.pow(b[j],2) < n:
            dem += 1
        else:break
print(dem)