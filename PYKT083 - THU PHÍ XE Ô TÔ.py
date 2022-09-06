m ={}
for j in range(int(input())):
    s = input().split()
    if s[3]=='IN':
        if s[1]=="Xe_con":
            if s[2] == '7':
                if s[4] in m:
                    m[s[4]] = m[s[4]]+15000
                else:
                    m[s[4]] = 15000
            else:
                if s[4] in m:
                    m[s[4]] = m[s[4]]+10000
                else:
                    m[s[4]] = 10000
        if s[1] =='Xe_tai':
            if s[4] in m:
                m[s[4]] = m[s[4]]+20000
            else:
                m[s[4]] = 20000
        if s[1]=="Xe_khach":
            if s[2] == '29':
                if s[4] in m:
                    m[s[4]] = m[s[4]]+50000
                else:
                    m[s[4]] = 50000
            else:
                if s[4] in m:
                    m[s[4]] = m[s[4]]+70000
                else:
                    m[s[4]] = 70000
for i in m:
    print("{}: {}".format(i,m[i]))
                
    