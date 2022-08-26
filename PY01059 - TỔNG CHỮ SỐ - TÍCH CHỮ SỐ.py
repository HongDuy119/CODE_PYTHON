for j in range(int(input())):
    n = input()
    sum = 0
    tich = 1
    kq = 0
    for i in range(len(n)):
        if i%2 ==0:
            sum += int(n[i])
        if i%2 == 1 and int(n[i])!=0:
            kq = 1
            tich *= int(n[i])
    if kq == 0:
        tich = 0
    print(sum,tich)