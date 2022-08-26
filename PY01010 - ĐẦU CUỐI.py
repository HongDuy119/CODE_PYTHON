test = int(input())
while test>0:
	string = input()
	a = int(len(string))
	if string[0]==string[a-2] and string[1]==string[a-1]:
		print("YES")
	else: print("NO")
	test -= 1
