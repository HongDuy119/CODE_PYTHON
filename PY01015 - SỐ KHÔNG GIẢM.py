def sokhonggiam(n):
	for i in range(len(n)-1):
		if n[i+1] < n[i]:
			return 0
	return 1

test = int(input())
while (test>0) :
	n = input()
	check = sokhonggiam(n)
	if check==1: print("YES")
	else: print("NO")
	test -= 1