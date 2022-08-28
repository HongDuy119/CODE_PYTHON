for i in range(int(input())):
    n = input()
    sum = 0
    multiple = 1
    for j in range(len(n)):
        if j%2==0 and int(n[j])!=0:
            multiple *= int(n[j])
        if j%2 != 0:
            sum += int(n[j])
    print(multiple,sum)