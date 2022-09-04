text =""
while True: 
    try:
        text += input()
    except EOFError:
        break
text=text.replace('?','.')
text=text.replace('!','.')
text = text.lower().split('.')
# print(text)
for i in range(len(text)-1):
    x = text[i].lower().split()
    x[0] = x[0].title()
    print(' '.join(x))
    
    
                    # author HongDuy