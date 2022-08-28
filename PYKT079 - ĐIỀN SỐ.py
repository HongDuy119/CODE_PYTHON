for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * 1000005
    for j in a:
        b[j] = 1
    res = 0
    for j in range(min(a),max(a)):
        if b[j] == 0:
            res += 1
    print(res)