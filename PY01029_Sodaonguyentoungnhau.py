from audioop import reverse


def ucln(a,b):
    if b==0 :
        return a
    return ucln(b,a%b)
def so_nguoc(a):
    sum = 0
    while a > 0:
        sum = sum*10 + a%10
        a = a//10
    # print(sum)
    return sum

for i in range(int(input())) :
    n = int(input())
    a = so_nguoc(n)
    if ucln(n,a)== 1:
        print("YES")
    else: print("NO")
    