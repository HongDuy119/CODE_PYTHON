def check(a):
    for i in range(2,len(a),2):
        if a[i]!=a[0]:
            return False
    for i in range(1,len(a),2):
        if a[i]!=a[1]:
            return False
    return True
for i in range(int(input())):
    n = input()
    if check(n):
        print("YES");
    else: print("NO")