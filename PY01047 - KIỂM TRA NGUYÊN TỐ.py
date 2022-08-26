import math
def nguyen_to(a):
    if(a<2): return False
    for i in range(2,int(math.sqrt(a))+1,1):
        if a%i==0: return False
    return True
for i in range(int(input())):
    String = input()
    sum = 0
    for j in range(len(String)-4,len(String)):
        sum = sum*10+int(String[j])
    if(nguyen_to(sum)): print("YES")
    else: print("NO")