from math import gcd


a,b = [int(x) for x in input().split()]
gcdd = gcd(a,b)
print("{}/{}".format(a//gcdd,b//gcdd))