while True:
    string = input()
    if len(string.split())==1:
        break;
    [p,q] = string.split()
    p = int(p)
    q = str(q)
    mau = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    res = ""
    for i in range(len(q)):
        res = str(mau[(mau.index(q[i])+p)%28])+res
    print(res)