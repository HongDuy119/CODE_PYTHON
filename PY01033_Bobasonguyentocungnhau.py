import math

[p,q] = input().split()
p , q = int(p),int(q)
for i in range(p,q+1,1):
    for j in range(i+1,q+1,1):
        if math.gcd(i,j)==1:
            for k in range(j+1,q+1,1):
              if math.gcd(i,j)==1 and math.gcd(i,k)==1 and math.gcd(j,k)==1:
                print("({0}, {1}, {2})".format(i,j,k))