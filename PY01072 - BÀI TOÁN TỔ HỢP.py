n , k = [int(x) for x in input().split()]
c = list(map(int,input().split()))
a ={}
for i in c: 
    a[i]=1
a = sorted(a)
b = [0]*1005
def In():
    for i in range(1,k+1):
        print(a[b[i]-1],end =" ")
    print()
def Try(i):
    for j in range(b[i-1]+1,len(a)-k+i+1):
        b[i] = j
        if i==k: In()
        else: Try(i+1)
Try(1)