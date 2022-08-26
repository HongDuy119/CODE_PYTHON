from re import I


for j in range(int(input())):
    p, q = [int(x) for x in input().split()]
    dem = 0
    for i in range(2,p+1,1):
        n = i
        while n%q == 0:
            dem += 1
            n /= q
    print(dem)            