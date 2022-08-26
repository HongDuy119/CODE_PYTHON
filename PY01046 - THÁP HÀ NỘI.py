def chuyen(a,c):
    print(a + " -> " +c)
def thap_Ha_Noi(n , a , b , c):
    if n ==1 :
        chuyen(a,c)
    else:
        thap_Ha_Noi(n-1,a,c,b)
        chuyen(a,c)
        thap_Ha_Noi(n-1,b,a,c)
n = int(input())
thap_Ha_Noi(n,'A','B','C')