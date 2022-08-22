import math
def so_nguoc(a):
    sum = 0
    while a > 0:
        sum = sum*10 + a%10
        a = a//10
    # print(sum)
    return sum
def nguyen_to(a):
    if(a<2): return False
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0: return False
    return True
def kt(a):
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
        if nguyen_to(int(a[i])) == False: return False
    if nguyen_to(sum):return True
    return False
for i in range(int(input())):
    a = int(input())
    b = so_nguoc(a)
    c = str(a)
    if nguyen_to(a) and nguyen_to(b) and kt(c): print("Yes")
    else: print("No")
