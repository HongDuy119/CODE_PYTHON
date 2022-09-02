def check(a):
    if len(a)!=4:
        return False
    else:
        for x in a:
            if x.isdigit():
                if int(x)<0 or int(x)>255:
                    return False
            else:
                return False
    return True
for j in range(int(input())):
    s = input()
    a = s.split('.')
    if check(a):
        print("YES")
    else:
        print("NO")