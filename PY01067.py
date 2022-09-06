demm = 0
n = 0
def Try(s,d2):
    print(1)
    print(demm,n)
    # if dem<n and d2>int(len(s)/2) and d2>0:
    #     print(s,end =" ")
    #     dem += 1
    demm += 1
    
    Try(s+'0',d2)
    Try(s+'1',d2)
    Try(s+'2',d2+1)
    if demm == n:
        return
for j in range(int(input())):
    n = int(input())
    demm = 0
    Try("",0)