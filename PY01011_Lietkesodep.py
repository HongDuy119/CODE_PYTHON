def bool(a):
    b = str(a)
    if len(b)%2 == 1:
        return False;
    for i in range(len(b)):
        if b[i] != b[len(b)-i-1]: return False
        if int(b[i]) %2 != 0: return False
    return True


for i in range(int(input())):
    n = int(input())
    for j in range(22,n,2):
        if bool(j): print(j,end=" ")
    print("")   