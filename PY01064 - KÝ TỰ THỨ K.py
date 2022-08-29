for i in range(int(input())):
    a , b = [int(x) for x in input().split()]
    dem = 0
    while b%2==0:
        dem += 1
        b = b//2
    print(chr(ord('A')+dem))