def check(n):
    if len(n)%2==0:
        print("NO")
        return
    if n[0]==n[1] :
        print("NO")
        return
    for i in range(0,len(n),2):
        if n[i] != n[0]: 
            print("NO")
            return
    print("YES")
for i in range(int(input())):
    n = input()
    check(n)