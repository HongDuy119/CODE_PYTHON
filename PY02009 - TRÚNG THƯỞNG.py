for j in range(int(input())):
    n = int(input())
    a = [0]*1005
    for i in range(n):
        a[int(input())] += 1
    b = []
    c=[]
    for i in range(1,1001,1):
        if a[i]!=0:
            c.append(i)
            b.append(a[i])
    b.sort(reverse=True)
    for i in c:
        if a[i] == b[0]:
            print(i)
            break;
    
    