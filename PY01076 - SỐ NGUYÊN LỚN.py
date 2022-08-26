from math import gcd


def ucln(a , b):
    k =gcd(a,b)
    return k
for i in range(int(input())):
    a = int(input())
    b = int(input())
    print(ucln(a,b))