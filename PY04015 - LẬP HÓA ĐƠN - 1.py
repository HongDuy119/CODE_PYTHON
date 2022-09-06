a = []
n = int(input())
for i in range(n):
    name = input()
    cu = int(input())
    moi = int(input())
    a.append([])
    if i<9:
        strr = 'KH0'+str(i+1)
        a[i].append(strr)  
    else:
        strr = 'KH'+str(i+1)
        a[i].append(strr)
    a[i].append(name)
    chi_so = moi-cu
    if chi_so >100:
        chi_so = 50*100+50*150+(chi_so-100)*200
        chi_so += chi_so*0.05
    elif chi_so>=51:
        chi_so = 50*100+(chi_so-50)*150
        chi_so += chi_so*0.03
    else:
        chi_so = 100*chi_so
        chi_so += chi_so*0.02
    chi_so = round(chi_so)
    a[i].append(chi_so)
b = sorted(a,key = lambda x:(-x[2]))
for i in b:
    print(i[0],i[1],i[2])