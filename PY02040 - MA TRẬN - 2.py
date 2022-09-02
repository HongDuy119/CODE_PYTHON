n = int(input())
a = []
for i in range(n):
    a.append(input())
k = int(input())
sum1 = sum2 = 0
for i in range(n):
    s = a[i].split()
    for j in range(len(s)):
        if i<(n-j-1):
            sum1 += int(s[j])
        elif i>(n-j-1):
            sum2 += int(s[j])
            
if k<abs(sum1-sum2):
    print("NO")
    print(abs(sum1-sum2))
else:
    print("YES")
    print(abs(sum1 - sum2))

                            # author HongDuy