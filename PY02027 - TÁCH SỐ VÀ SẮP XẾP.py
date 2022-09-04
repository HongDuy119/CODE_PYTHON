a = []
for j in range(int(input())):
    s = input()+"d"
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit():
            sum = sum*10+int(s[i])
            if s[i+1].isalpha():
                a.append(sum)
                sum = 0
a.sort()
for i in a:
    print(i)
    