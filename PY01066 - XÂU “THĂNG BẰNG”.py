for j in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b =[]
    b.append(0)
    d = [0]*100005
    d[0] = 1
    for i in range(len(a)):
        while len(b)!=0:
            if a[i]>a[b[-1]]:
                d[i] = d[i]+d[b[-1]]
                b.pop()
            else:break
        b.append(i)
    for i in d:
        print(i,end=" ")
    print("")
                
            