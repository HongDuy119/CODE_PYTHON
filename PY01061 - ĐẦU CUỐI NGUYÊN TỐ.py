import math


def nguyen_to(n):
    if n< 2 : return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i == 0:
            return False
    return True
for i in range(int(input())):
    n = input()
    n1 = n2 = 0
    for j in range(3):
        n1 = n1*10+int(n[j])
    for j in range(len(n)-3,len(n)):
        n2 = n2*10 +int(n[j])
    if nguyen_to(n1) and nguyen_to(n2):
        print("YES")
    else: print("NO")