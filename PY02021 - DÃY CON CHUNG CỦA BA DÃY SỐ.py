for j in range(int(input())):
    n = input()
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    # print(a[1])
    n1 = n2 = n3 =0
    kq=0
    while n1<len(a) and n2<len(b) and n3<len(c):
        maxN = max(a[n1],b[n2],c[n3])
        if a[n1] == b[n2] and a[n1] ==c[n3] and b[n2] == c[n3]:
            print(a[n1],end=" ")
            kq=1
            n1 += 1
            n2+=1
            n3+=1
        elif a[n1]<maxN: n1+=1
        elif b[n2]<maxN: n2+=1
        elif c[n3]<maxN: n3+=1
    if kq==0: print("NO",end="")    
    print()