test = int(input())
a = list(map(int,input().split()))    
c = [0] *(max(a)+4)
for i in a:
    c[i] = 1
for i in range(1,max(a)+2,1):
    if c[i] == 0:
        print(i)
        break

    