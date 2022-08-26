a = [1]*100
a[0] =0
a[1] = 1
for i in range(2,93,1):
    a[i] = a[i-1]+a[i-2]
for i in range(int(input())):
    p , q = [int(x) for x in input().split() ]
    for j in range(p,q+1,1):
        print(a[j],end=" ")
    print("")