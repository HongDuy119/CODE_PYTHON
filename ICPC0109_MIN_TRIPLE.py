for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    min1 , min2, min3 = int(1e8) ,int(1e8) ,int(1e8)
    k = z = 0
    for i in range(n):
        if a[i]<min1:
            min1 = a[i]
            k = i 
    a[k] = int(1e8)
    for i in range(n):
        if a[i]<min2:
            min2 = a[i]
            z = i
    a[z] = int(1e8)
    for i in a:
        if i<min3:
            min3 = i
    print(min1+min2+min3)