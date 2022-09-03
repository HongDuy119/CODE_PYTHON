import math
def nguyen_to(a):
    if(a<2): return False
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0: return False
    return True
n = int(input())
a = [0]*100005
duy = []
sum = 0
b = list(map(int,input().split()))
for i in b:
    if a[i] ==0:
        duy.append(i)
        sum += i
    a[i] = 1
sum1 = 0
kq = 1
for i in range(len(duy)):
    sum1 += duy[i]
    if nguyen_to(sum1) and nguyen_to(sum-sum1):
        kq = 0
        print(i) 
        break
if kq==1:
    print("NOT FOUND")