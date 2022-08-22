a = [1]*1000005
a[0] , a[1] = 0,0
for i in range(2,int(1e6),1):
    if a[i]==1:
        for j in range(i*2,int(1e6),i):
            a[j] = 0
def ucln(n,k):
    if(k==0): return n
    return ucln(k,n%k)
for i in range(int(input())):
    [p,q] = input().split()
    p,q = int(p),int(q)
    k = str(ucln(p,q))
    sum = 0
    for j in k:
        sum += int(j)
    if a[sum]==1: print("YES")
    else: print("NO")
     