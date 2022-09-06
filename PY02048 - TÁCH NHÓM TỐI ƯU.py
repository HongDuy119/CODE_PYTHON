n,k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
res = 1
for i in range(1,n):
    if a[i]-a[i-1]>k: res+=1
print(res)