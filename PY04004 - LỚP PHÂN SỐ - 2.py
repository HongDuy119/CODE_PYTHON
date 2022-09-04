from math import gcd
from posixpath import split


a , b , c, d = [int(x) for x in input().split()]
a = a*d + c*b
b = b*d
gcdd = gcd(a,b)
print("{}/{}".format(a//gcdd,b//gcdd))
