text =[]
while True: 
    try:
        text.append(input())
    except EOFError:
        break
for i in range(0,len(text),1):
    if text[i][-1]!='.' and text[i][-1]!='?' and text[i][-1]!='!':
        text[i] = text[i]+'.'
    x = text[i].lower().split()
    x[0] = x[0].title()
    for j in range(len(x)):
        # print(x[j])
        if j==len(x)-2 and (x[j+1]=='.' or x[j+1]=='!' or x[j+1]=='?'):
            print(x[j],end="")
            print(x[j+1])   
            break
        elif j==len(x)-1:
            print(x[j])
        else:
            print(x[j],end=" ")
    
    
                    # author HongDuy