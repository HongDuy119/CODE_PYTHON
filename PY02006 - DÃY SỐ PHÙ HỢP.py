for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = list(map(int,input().split()))
    b.sort()
    for j in range(len(a)):
        if a[j]>b[j]:
            print("NO")
            break
        if j == len(a)-1:
            print("YES")