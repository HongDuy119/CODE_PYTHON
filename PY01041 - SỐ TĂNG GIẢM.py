def tang(a):
    for i in range(0,len(a)-1,1):
        if a[i]>= a[i+1]:
            return False
    return True
def giam(a):
    for i in range(0,len(a)-1,1):
        if a[i]<= a[i+1]:
            return False
    return True
for j in range(int(input())):
    n = input()
    res = "NO"
    for i in range(1,len(n)-1,1):
        n1 = n[0:i]
        n2 = n[i:]
        if tang(n1) and giam(n2):
            res =  "YES"
            break
    print(res)