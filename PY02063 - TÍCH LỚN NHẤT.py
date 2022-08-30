n = int(input())
a = list(map(int,input().split()))
b = sorted(list(a))
print(max(b[0]*b[1]*b[2] , b[0]*b[1] , b[-1]*b[-2]*b[-3] , b[0]*b[1]*b[-1]  ))