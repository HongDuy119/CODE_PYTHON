import math


for j in range(int(input())):
    n = input()
    nho = 0
    res = ""
    for i in range(len(n)-1,0,-1):
        if nho == 0:
            if n[i] < '5':
                res = '0' + res
                nho = 0
            elif n[i] >= '5':
                res = "0" + res
                nho = 1
        else:
            if n[i]>='4':
                res = '0' + res
                nho = 1
            elif n[i] <'4':
                res ='0'+ res
                nho = 0
    if nho == 0:
        print(n[0]+res)
        
    else:
        if n[0] =='9':
            res = '0'+res
            print("1"+res);
        else :
            res = chr(ord(n[0])+1) + res
            print(res)          
            
        
        