import math
from operator import truediv


def nguyen_to(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def check(n):
    for i in range(len(n)):
        if nguyen_to(i) and not(nguyen_to(int(n[i]))):
            return False
        if not(nguyen_to(i)) and nguyen_to(int(n[i])):
            return False
    return True
for i in range(int(input())):
    n = input()
    if check(n): print("YES")
    else: print("NO")