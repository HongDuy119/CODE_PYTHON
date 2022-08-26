from pickletools import stringnl_noescape


for i in range(int(input())):
    string = input()
    if string[len(string-2)=='8'] and string[len(string-1)=='6']: print("YES")
    else:print("NO")