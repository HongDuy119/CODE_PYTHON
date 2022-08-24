from tokenize import Double


for j in range(int(input())):
    n , x ,m = [float(k) for k in input().split()]
    for i in range(1,1000 , 1):
        if n*((1+x/100)**i) >= m:
            print(i)
            break