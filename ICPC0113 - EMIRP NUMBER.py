import math
a =[1] * 1000005
a[0] = a[1] =  0
for i in range(2,int(1e6),1):
    if a[i] == 1:
        for j in range(i*2,int(1e6),i):
            a[j] = 0
def bool(n,k):
    n = str(n)
    res=""
    for i in n:
        res = str(i) + res
    if res <= n or int(res)>int(k) or a[int(n)]==0 or a[int(res)]==0:
        return  
    print(n+" " +res, end = " ")
for i in range(int(input())):
    string = input()
    for j in range(13,int(string),1):
        bool(j,string)
    print("")
        