import math


def nguyen_to(n):
    if n<2 : return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
for i in range(int(input())):
    n = input()
    sum = 0
    for j in n:
        sum += int(j)
    if nguyen_to(sum): print("YES")
    else: print("NO")