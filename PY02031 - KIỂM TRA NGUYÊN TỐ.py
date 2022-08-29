import math
def nguyen_to(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True
n,m = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(input())
for i in a:
    for j in i.split():
        if nguyen_to(int(j)): print("1",end=" ")
        else: print("0",end=" ")
    print("")