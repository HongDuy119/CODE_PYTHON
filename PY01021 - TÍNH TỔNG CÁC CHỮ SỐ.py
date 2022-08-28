for i in range(int(input())):
    n = input()
    sum = 0
    a = []
    for j in n:
        if j.isdigit():
            sum += int(j)
        else:
            a.append(j)
    a.sort()
    for j in a:
        print(j,end="")
    print(sum)