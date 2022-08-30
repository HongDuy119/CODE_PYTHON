

for t in range(int(input())):
    s = input()
    s = list(s)
    k = len(s)-1
    while(s[k-1]<=s[k] and k>0):
        k -= 1
    i = k
    k -= 1
    if k<0 :
        print("-1")
    else:
        min = 0
        p = 0
        for i in range(k+1,len(s)):
            if s[i]<s[k] and ord(s[i]) > min:
                min = ord(s[i])
                p = i
        if k == 0 and s[p]=='0':
            print("-1")
        else:
            s[k] , s[p] = s[p] , s[k]
            print("".join(s))

    
