
a = {}
n = int(input())
for i in range(n):
    district = input()
    start = [int(x) for x in input().split(':')]
    end = [int(x) for x in input().split(':')]
    amount = int(input())
    if district in a:
        a[district] =((end[0]*60+end[1]-start[0]*60-start[1])+a[district][0],amount+a[district][1])
    else:
        a[district] =((end[0]*60+end[1]-start[0]*60-start[1]),amount)
res = 1
for i in a:
    print("T0{}".format(res),end=" ")
    print(i,"{:.2f}".format((a[i][1]/a[i][0])*60))
    res += 1