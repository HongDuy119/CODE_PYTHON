def sum(n):
    sum1 = 0
    for i in n:
        sum1 += int(i)
    return sum1
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for j in range(1000):
        for k in a:
            if sum(str(k))==j: print(k,end=" ")
    print(" ")