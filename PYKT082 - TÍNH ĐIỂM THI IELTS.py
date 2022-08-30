for i in range(int(input())):
    a = list(input().split())
    R , L = int(a[0]) , int(a[1])
    S , W = float(a[2]) , float(a[3])
    b = [1.0,1.0,1.0,2.5,2.5,3.0,3.0,3.5,3.5,3.5,4.0,4.0,4.0,4.5,4.5,4.5,5.0,5.0,5.0,5.0,5.5,5.5,5.5,6.0,6.0,6.0,6.0,6.5,6.5,6.5,7.0,7.0,7.0,7.5,7.5,8.0,8.0,8.5,8.5,9.0,9.0];
    res = float((S+W+b[R]+b[L])/4)
    res = round(res,2)
    c = str(res).split('.')
    res = round(res,2)
    if int(c[1])<25:
        print(c[0]+'.0')
    elif int(c[1])>=25 and int(c[1])<75:
        print(c[0]+'.5')
    elif int(c[1])>=75:
        print(int(c[0])+1,end=".0")
        print("")
        
        
    
    