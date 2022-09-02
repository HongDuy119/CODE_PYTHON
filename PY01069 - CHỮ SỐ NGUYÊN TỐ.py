k = int(input())
def Try(s,d2,d3,d5,d7):
    if len(s) == n and d2>0 and d3>0 and d5>0 and d7>0 and int(s[n-1])%2==1:
        print(s)
    elif len(s)<n:
        Try(s +'2',d2+1,d3,d5,d7)
        Try(s +'3',d2,d3+1,d5,d7)
        Try(s +'5',d2,d3,d5+1,d7)
        Try(s +'7',d2,d3,d5,d7+1)
for i in range(4,k+1):
    n = i
    Try("",0,0,0,0)
        
        