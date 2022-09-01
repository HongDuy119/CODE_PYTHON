def multiple2(n):
    multiple1 = 1
    while n>0:
        multiple1 *= n%10
        n = n//10
    return multiple1
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a.sort(key=multiple2)
    for k in a:
        print(k,end=" ")
    print()
    
    
    
                                        # author HongDuy