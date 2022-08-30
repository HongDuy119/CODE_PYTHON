while True:
    n = int(input())
    if n ==0:
        break
    a = {}
    for i in range(n):
        a[int(input())] = 1
    if len(a)==1:
        print("BANG NHAU")
    else:
        b = sorted(list(a))
        print(b[0],b[-1])
            