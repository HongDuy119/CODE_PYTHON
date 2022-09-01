n = [str(x) for x in input().lower().split()]
s = [str(x) for x in input().lower().split()]
b =set()
c = set()
for i in n:
    c.add(i)
for i in s:
    if not(i in n):
        c.add(i)
for i in s:
    if i in n:
       b.add(i)
b = sorted(b)
c = sorted(c)
for i in c:
    print(i,end=" ")
print()
for i in b:
    print(i,end = " ")
    