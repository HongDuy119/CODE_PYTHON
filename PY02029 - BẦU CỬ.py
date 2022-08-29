n , m = [int(x) for x in input().split()]
a = list(map(int,input().split()))
b =[0]*(m+1)
c = []
d = [0]*(m+1)
for i in a:
    b[i] += 1
    d[i] += 1
a.sort(),b.sort(reverse=True)
# print(b)
for i in b : 
    if len(c)==0 :
        if i!=0:
            c.append(i)
    else:
        # print(c[-1],i)
        if c[-1] != i and i!=0:
           c.append(i)
# print(c)
if len(c) <=1:
    print('NONE')
else:
    for i in a:
        if d[i] == c[1]:
            print(i)
            break
        


    