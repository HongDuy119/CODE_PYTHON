n,k = [int(x) for x in input().split()]
a = [str(s) for s in input().split()]
b = set()
d = [0]*1005
for i in a:
    b.add(i)
c = sorted(b)
n = len(c)
def In():
    for i in range(1,k+1):
        print(c[d[i]-1],end=" ")
    print()
def Try(i):
    for j in range(d[i-1]+1,n-k+i+1):
        d[i] = j
        if i==k: In()
        else:Try(i+1)
Try(1)
                    # author HongDuy
