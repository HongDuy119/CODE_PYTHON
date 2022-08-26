import math

for t in range(int(input())):
    n = int(input())
    print(1,end=" ")
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            dem=0
            while n% i == 0:
                dem += 1
                n //= i
            print("* {}^{}".format(i,dem),end=" ")
    if n > 1 :
        print("* {}^1".format(n),end=" ")
    print()