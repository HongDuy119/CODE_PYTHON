import math
string =""
def nguyen_to(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1,1):
        if n%i==0: return False
    return True
def solve():
    if nguyen_to(len(string))==False:
        print("NO")
        return
    dem = 0 
    for i in string:
        if nguyen_to(int(i)):
            dem += 1
    if dem<(len(string)-dem):
        print("NO")
        return
    print("YES")
        
for i in range(int(input())):
    string = input()
    solve()