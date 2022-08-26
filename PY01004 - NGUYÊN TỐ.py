import math
from re import S
def nguyen_to(a):
    if(a<2): return False
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0: return False
    return True
def ucln(a,b):
    if b==0: return a
    return ucln(b,a%b)
for i in range(int(input())):
    a = int(input())
    res = 0
    for j in range(a):
        if ucln(a,j) == 1: res += 1
    if(nguyen_to(res)): print("YES")
    else: print("NO")