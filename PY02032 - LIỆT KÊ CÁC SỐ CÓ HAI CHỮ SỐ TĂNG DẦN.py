n = input()
a = set()
res = ""
for i in range(len(n)):
    if i%2==0:
        res = res +"."
    res += n[i]
# print(res)
b = res.split('.')
for i in b:
    if len(i)==2:
        a.add(i)
a = sorted(a)
for i in a:
    print(i,end=" ")

                            # author HongDuy