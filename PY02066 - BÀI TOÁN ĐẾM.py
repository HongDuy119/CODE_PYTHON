n = int(input())
dem = 0
a = [0]*10005
maxN=0
while dem<n:
    s = list(map(int,input().split()))
    maxN = max(maxN,max(s))
    dem += len(s)
    for i in s:
        a[i] = 1
kq = 1
for i in range(1,maxN+1):
    if a[i] ==0:
        kq = 0
        print(i)
if kq ==1:
    print("Excellent!")
    