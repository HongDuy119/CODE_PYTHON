string = input()

dem = 0
for i in range(len(string)):
	if string[i]=='4' or string[i]=='7':
		dem += 1
if dem==4 or dem==7:
	print("YES")
else: print("NO")
