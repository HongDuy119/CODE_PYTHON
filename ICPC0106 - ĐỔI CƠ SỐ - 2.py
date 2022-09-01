def doi_co_so(p,q):
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
for i in range(int(input())):
    p = int(input())
    q = 0
    k = input()
    for i in range(len(k)):
        if int(k[i])==1:
            q = q + 2**(len(k)-int(i)-1)
    doi_co_so(p,q)