from operator import mul


for i in range(int(input())):
    string = input()
    multiply = 1
    for j in string:
        if j != '0':
            multiply *= int(j)
    print(multiply)