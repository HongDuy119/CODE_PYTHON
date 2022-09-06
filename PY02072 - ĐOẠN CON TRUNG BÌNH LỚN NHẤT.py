n = int(input())
a = [int(x) for x in input().split()]
dem = 0
res = 0
a.append(-int(1e6))
maxN = max(a)
for i in range(len(a)-1):
    if a[i]==maxN:
        dem += 1
        if a[i+1] != maxN:
            res = max(res,dem)
            dem = 0
print(res)