for j in range(int(input())):
    n , k = [int(x) for x in input().split()]
    a = list(map(int,input().split()))
    b = []
    c = []
    res = max(a)
    k1 = 0
    for i in a:
        if i<0:
            b.append(i)
        else:
            c.append(i)
    for i in b:
        if i==res and k1==0:
            print(k,i,end=" ")
            k1=1
        else:
            print(i,end=" ")
    for i in c:
        if i==res and k1==0:
            print(k,i,end=" ")
            k1=1
        else:
            print(i,end=" ")
    print()