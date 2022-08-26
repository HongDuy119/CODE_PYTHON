for j in range(int(input())):
    n1 = input()
    n2 = n1[::-1]
    res = "YES"
    for i in range(1,len(n1),1):
        if abs(int(ord(n1[i])-ord(n1[i-1]))) != abs(int(ord(n2[i])-ord(n2[i-1]))):
            res = "NO"
            break
    print(res)      