import math


def nguyen_to(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def check(n):
    if not(nguyen_to(len(n))):
        return False
    sum = 0
    for i in n:
        if nguyen_to(int(i)): sum += 1
    if sum <= (len(n)-sum):
        return False
    return True
for i in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else: print("NO")