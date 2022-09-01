for j in range(1,int(input())+1):
    s1 = input()
    s2 = input()
    a,b=[],[]
    for i in s1:
        a.append(i)
    for i in s2:
        b.append(i)
    a.sort()
    b.sort()
    print("Test {}: ".format(j),end="")
    if a==b:
        print("YES")
    else: print("NO")