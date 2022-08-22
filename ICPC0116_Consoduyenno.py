test = int(input())
while test>0 :
	string = input()
	if string[0]==string[len(string)-1]:
		print("YES")
	else: print("NO")
	test -= 1
