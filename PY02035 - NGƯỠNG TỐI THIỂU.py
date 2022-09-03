n = input()
k = int(input())
a = {}
res = ""
for i in range(len(n)):
    if i%2==0:
        res = res +"."
    res += n[i]
# print(res)
b = res.split('.')
b.sort()
for i in b:
    if len(i)==2:
        a[i] = 1
for i in b:
    if len(i)==2:
        a[i] +=1
# a = sorted(list(a))
kq = 0
for i in a:
    if a[i]-1>=k:
        print(i,a[i]-1)
        kq = 1
if kq == 0: print("NOT FOUND")

                            # author HongDuy