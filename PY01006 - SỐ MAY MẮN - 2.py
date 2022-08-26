test = int(input())
while test>0:
	string = input()
	kq =1;
	for i in range(len(string)):
		if string[i] != '4' and string[i] !='7':
			kq=0
	if kq==0: print("NO")
	else: print("YES")
	test -= 1