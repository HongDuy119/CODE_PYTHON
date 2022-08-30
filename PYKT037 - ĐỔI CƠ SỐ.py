for j in range(int(input())):
    q , p = [int(x) for x in input().split()]
    a = []
    while q>0:
        k = q%p
        if k>=10:
            a.append(chr(ord('A')+k-10))
        else: a.append(k)
        q //= p
    for i in range(len(a)-1,-1,-1):
        print(a[i],end="")
    print("")