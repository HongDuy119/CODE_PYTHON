def giai_thua(n):
    if n <= 1: return 1
    return n*giai_thua(n-1)
def to_hop(n):
    if n<2: return 0
    c = giai_thua(n)//(2*giai_thua(n-2))
    return c
n = int(input())
a = []
res = 0
for i in range(n):
    s = input()
    a.append(s)
for i in a:
    s = i
    dem = 0
    for j in s:
        if j=='C': dem += 1
    res += to_hop(dem)
for i in range(n):
    dem = 0
    for j in range(n): 
        if a[j][i] == 'C': dem += 1
    # print(dem)
    res += to_hop(dem)
print(res)
                        # author HongDuy