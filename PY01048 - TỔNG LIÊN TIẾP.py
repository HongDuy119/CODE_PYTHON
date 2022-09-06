import math
for j in range(int(input())):
    n = int(input())
    res = 0
    for i in range(1,int(math.sqrt(2*n))+1):
        if (2*n)%i ==0:
            if (i+(2*n)//i)%2==1:
                b = (i-1+(2*n)//i)//2
                a = (2*n)//i-b
                if b>a:
                    res +=1
    print(res)