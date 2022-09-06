a =[]
n = int(input())
for i in range(n):
    id = input()    
    name = input()
    start = [int(x) for x in input().split(':')]
    end = [int(x) for x in input().split(':')]
    a.append([])
    a[i].append(id)
    a[i].append(name)
    a[i].append(end[0]*60+end[1]-start[0]*60-start[1])
b = sorted(a,key = lambda x : (-x[2]))
for i in b:
    print(i[0],i[1],"{} gio {} phut".format(int(i[2]/60),i[2]%60))
    # print(i)
    
                                # author HongDUy