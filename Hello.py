def is_finite(num):
    x=0
    while(num!=0 and x!=num):
        x=num
        num=sum_divisors(num)

    if num==0 :
        return True
    else:
        return False

def sum_divisors(n):
    sum=1
    x=int(n**0.5)
    for i in range(2,(x//1)+1):
        if n%i==0:
            sum=sum+i
        if n%i==0 and n/i!=i:
            sum=sum+(n/i)            
    return int(sum)
sum1 = 0
for i in range(int(input())):
    n = int(input())
    # print(Sum(n))
    sum1 += sum_divisors(n)    
print(sum1)
