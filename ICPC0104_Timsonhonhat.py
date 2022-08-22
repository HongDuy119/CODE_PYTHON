

for i in range(int(input())) :
    string = input()
    res = 10**18
    string += 'd'
    sum = 0
    for i in range(len(string)):
        if string[i].isdigit():
            sum = sum*10+int(string[i])
            if string[i+1].isalpha():
                res = min(res,sum)
                sum = 0
    print(res)