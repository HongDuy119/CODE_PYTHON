test = int(input())
for i in range(test):
    sum = int(input())
    while sum%7 != 0:
        sum = sum + int(str(sum)[::-1])
    print(sum)