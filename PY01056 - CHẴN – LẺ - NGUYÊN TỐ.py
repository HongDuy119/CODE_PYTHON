import math


def nguyen_to(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
for i in range(int(int(input()))):
    n = input()
    sum = 0
    for j in range(len(n)):
        if j%2 == 0 and int(n[j])%2 == 1:
            sum = 0
            break
        if j%2 == 1 and int(n[j])%2 == 0:
            sum = 0
            break
        sum += int(n[j])
    if nguyen_to(sum): print("YES")
    else: print("NO")