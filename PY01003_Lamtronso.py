for i in range(int(input())):
    n = int(input())
    n1 = str(n)
    print(int(round(n,-len(n1)+1)))