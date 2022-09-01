from re import A


n , m = [int(x) for x in input().split()]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c ,d = {}, {}
for i in a : c[i] = 1
for i in b : d[i] = 1
for i in sorted(list(c)) :
    if i in d : print(i, end = ' ')
print()
for i in sorted(list(c)) :
    if not(i in d) : print(i, end = ' ')
print()
for i in sorted(list(d)) :
    if not(i in c) : print(i, end = ' ')