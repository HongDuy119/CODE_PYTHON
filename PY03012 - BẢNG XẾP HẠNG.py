res = []
nop = []
for i in range(int(input())):
    ten = input()
    sub = input()
    res.append(ten+" "+sub)
    nop.append(sub)
for i in range(len(res)):
    for j in range(i+1,len(res)):
        p1,p2 = [int(x) for x in nop[i].split()]
        q1 , q2 = [int(x) for x in nop[j].split()]
        if p1<q1:
            res[i] , res [j] = res[j] , res[i]
        elif p1==q1:
            if p2 >q2:
                res[i] , res [j] = res[j] , res[i]
for i in range(len(res)):
    print(res[i])