for i in range(int(input())):
    string = input()
    sum = 0
    for j in string:
        sum += int(j)
    if sum% 3 ==0 : print("YES")
    else: print("NO")