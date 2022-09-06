n = 0
a = [1]*1005
b = [1]*1005
res = []
def In():
    s = ''
    for i in range(1,n+1):
        s = s+str(a[i])
    res.append(s)
def Try(i):
    for j in range(n,0,-1):
        if b[j] ==1:
            a[i] = j
            b[j] = 0
            if i == n: In()
            else: Try(i+1)
            b[j] = 1 
for j in range(int(input())):
    n = int(input())
    res = []
    a = [1]*1005
    b = [1]*1005
    Try(1)
    print(len(res))
    print(' '.join(res))