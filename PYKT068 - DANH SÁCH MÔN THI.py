m = {}
for t in range(int(input())):
    s = input()
    a = input() + " "
    a = a + input()
    m[s] = a
a = sorted(list(m))
for i in a:
    print(i,m[i])