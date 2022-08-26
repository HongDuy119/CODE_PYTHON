
string = input()
lower,upper = 0,0
for i in string:
    if i.islower():
        lower += 1
    else : upper += 1
if lower >= upper : string = string.lower()
else: string = string.upper()
print(string)