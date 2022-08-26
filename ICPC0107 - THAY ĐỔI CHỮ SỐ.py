import math


for i in range(int(input())):
    [p,q] = list(map(str,input().split()))
    n1 = list(map(str,input().split()))
    if len(n1)==1:
        n2 = input()
        sum1 = int(n1[0].replace(p,q)) + int(n2.replace(p,q))
        sum2 =  int(n1[0].replace(q,p)) + int(n2.replace(q,p))
        print("{0} {1}".format(min(sum1,sum2) ,max(sum1,sum2)))
    else:
        sum1 = int(n1[0].replace(p,q)) + int(n1[1].replace(p,q))
        sum2 =  int(n1[0].replace(q,p)) + int(n1[1].replace(q,p))
        print("{0} {1}".format(min(sum1,sum2) ,max(sum1,sum2)))
        
        