import math


def nguyen_to(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
array = [0]*1000005
for i in a:
    array[i] += 1
for i in a:
    if nguyen_to(i) and array[i]!=0:
        print(i,array[i])
        array[i] = 0