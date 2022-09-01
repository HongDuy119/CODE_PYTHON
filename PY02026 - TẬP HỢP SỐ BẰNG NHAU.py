
n , m = [int(x) for x in input().split()]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c ,d = {}, {}
for i in a : c[i] = 1
for i in b : d[i] = 1
if c == d : print('YES')
else : print('NO')