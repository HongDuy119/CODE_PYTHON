for j in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    maxN = 0
    b = [0]*1000005
    for i in a:
        b[i] += 1
        maxN =max(maxN,b[i])
    a.sort()
    if maxN<= n//2: print("NO")
    else:
        for i in a:
            if b[i] == maxN:
                print(i)
                break