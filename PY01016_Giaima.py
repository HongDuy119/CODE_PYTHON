for i in range(int(input())):
    string = input()
    for j in range(len(string)):
        if string[j].isalpha():
            for k in range(int(string[j+1])):
                print(string[j],end="")
    print("")