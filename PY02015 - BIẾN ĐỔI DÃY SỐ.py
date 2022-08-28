while True:
    a , b , c , d = [int (x) for x in input().split()]
    if a == 0 and a==b and a== c and a==d:
        break
    dem = 0
    while True:
        a1 , b1, c1,d1 = a,b,c,d
        if a1==b1 and a1==c1 and a1==d1 and b1==c1 and b1==d1 and c1==d1:
            break
        dem += 1
        a = abs(a1-b1)
        b = abs(b1-c1)
        c = abs(c1-d1)
        d = abs(d1-a1)
    print(dem)