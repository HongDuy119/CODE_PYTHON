for i in range(int(input())):
    [n,d] = input().split()
    n, d = int(n), int(d)
    a = list(map(int,input().split()))
    for i in range(d,n):
        print(a[i], end = " ")
    for i in range(0,d):
        print(a[i], end = " ")
    print("")
    