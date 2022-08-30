import math


def nguyen_to(n):
    if n <2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
    if nguyen_to(i):
        b.append(i)
b.sort(reverse=True)
for i in a:
    if nguyen_to(i):
        print(b[-1],end=" ")
        b.pop()
    else:
        print(i,end=" ")
