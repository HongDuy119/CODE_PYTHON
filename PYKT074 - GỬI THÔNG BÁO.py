n = int(input())
a = []
for i in range(n):
    s = input().split()
    res = ""
    dem = 0
    for j in s:
        if dem+len(j)>100:
            break
        else:
            res = res+j+" "
            dem += len(j)+1
    a.append(res)
for i in a:
    print(i)
    