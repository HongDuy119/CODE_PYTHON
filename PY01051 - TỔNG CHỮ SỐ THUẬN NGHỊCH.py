for i in range(int(input())):
    n = input()
    sum = 0
    for l in n:
        sum += int(l)
    if sum == int(str(sum)[::-1]) and len(str(sum))>1:
        print("YES")
    else: print("NO")