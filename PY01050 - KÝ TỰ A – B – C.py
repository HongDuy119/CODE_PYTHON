from re import L


def boolen(s1,s2):
    for i in range(1,len(s1)):
        k = abs(int(ord(s1[i])) - int(ord(s1[i-1])))
        k1 = abs(int(ord(s2[i])) - int(ord(s2[i-1])))
        if k != k1:
            print("NO")
            return
    print("YES")
for i in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    boolen(s1,s2)
    