from tokenize import String


for i in range(int(input())):
    string = input()
    string = string+"-"
    dem = 1
    for j in range(len(string)-1):
        if string[j] != string[j+1]:
            print(dem,end = "")
            print(string[j],end="") 
            dem = 1
        else: dem += 1
    print("")
        
