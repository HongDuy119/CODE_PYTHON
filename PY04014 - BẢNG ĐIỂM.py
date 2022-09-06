from decimal import ROUND_HALF_UP, Decimal
a = []
n = int(input())
for i in range(n):
    name = input()
    diem = [Decimal(x) for x in input().split()]
    a.append([])
    if i<9:
        strr = 'HS0'+str(i+1)
        a[i].append(strr)  
    else:
        strr = 'HS'+str(i+1)
        a[i].append(strr)
    a[i].append(name)
    k = diem[0]*2+diem[1]*2+diem[2]+diem[3]+diem[4]+diem[5]+diem[6]+diem[7]+diem[8]+diem[9]
    k /= 12
    k = k.quantize(Decimal('0.1'), ROUND_HALF_UP)
    a[i].append(k)
    if k>=9:    
        a[i].append('XUAT SAC')
    elif k>=8:
        a[i].append("GIOI")
    elif k>=7:
        a[i].append("KHA")
    elif k>=5:
        a[i].append("TB")
    else:
        a[i].append("YEU")
b = sorted(a,key = lambda x:(-x[2]))
for i in b:
    print(i[0],i[1],i[2],i[3])
    