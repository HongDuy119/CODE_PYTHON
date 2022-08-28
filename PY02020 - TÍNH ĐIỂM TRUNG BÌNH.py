n = int(input())
c = list(map(float,input().split()))
a = []
for i in c:
    a.append(i)
a.sort()
sum = 0
dem = 0
for i in a:
    if i!=a[0] and i!=a[-1]:
        sum += i
        dem += 1
sum /= dem
print("{:.2f}".format(sum))