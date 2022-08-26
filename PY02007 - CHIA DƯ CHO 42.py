test = 10 
b = [1]*43
k = 0
for i in range(test):
    a = list(map(int,input().split()))
    k += len(a)
    for j in a:
        b[j%42] = 0
    if(k==10):break
k = 0
for i in range(0,42,1):
    if b[i] ==0: k+= 1
print(k)