def check(n):
    c = str(n)
    for i in range(len(c)):
        if int(c[i])%2==1:
            return False
    return True
for j in range(int(input())):
    n = int(input())
    a = []
    for i in range(2,888+1,2):
        if check(i):
            a.append(i)
    b= []
    for i in a:
        c = str(i) + str(i)[::-1]
        b.append(int(c))
    b.sort()
    for i in b:
        if i<n:
            print(i,end = " ")
    print("")
