mu2 = [2**x for x in range(66)]
mu3 = [3**x for x in range(39)]
mu5 = [5**x for x in range(27)]
a = {1:1}
for i in range(66): 
    for j in range(39):
        for k in range(27):
            tmp =mu2[i]*mu3[j]*mu5[k]
            if tmp <= 10**18:
                a[tmp] =1
m = sorted(list(a))
p = 1
for x in m:
    a[x] = p
    p += 1
for i in range(int(input())):
    n = int(input())
    if n in a:
        print(a[n])
    else:print("Not in sequence")
            
    