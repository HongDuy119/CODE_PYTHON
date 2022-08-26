for i in range(int(input())):
    n = input()
    kq = 1
    for j in n:
        if j!='0' and j!='1' and j!='2':
            print("NO")
            kq= 0
            break;
    if kq ==1: print("YES")    
    