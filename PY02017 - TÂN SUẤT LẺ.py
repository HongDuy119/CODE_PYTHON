for j in range(int(input())):
    n = int(input())
    b = [0]*1000005
    a = list(map(int,input().split()))
    for i in a:
        b[i] += 1
    for i in a:
        if b[i]%2 == 1:
            print(i)
            break