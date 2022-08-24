
def Sum(N):
      
    SumOfPrimeDivisors = [0] * (N + 1)  
    for i in range(2, N + 1) :
        if (SumOfPrimeDivisors[i] == 0) :
            for j in range(i, N + 1, i) :
                SumOfPrimeDivisors[j] = i
    return SumOfPrimeDivisors[N]
sum1 = 0
for i in range(int(input())):
    n = int(input())
    while n!=1 :
        sum1 += Sum(n)
        n = int(n/Sum(n))
print(sum1)