def ucln(a,b):
    if(b==0): return a
    return ucln(b,a%b)

[p,q] = input().split()
p , q = int(p),int(q)
dem = 0
for i in range(10**(q-1),10**q,1):
    if ucln(i,p) == 1:
        dem += 1
        print(i,end=" ")
    if dem!=0 and dem%10 == 0:
        print(" ")
        dem=0