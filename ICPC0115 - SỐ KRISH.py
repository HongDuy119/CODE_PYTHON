def giai_thua(n):
	if n==1 or n==0 : return 1
	return n*giai_thua(n-1)
test = int(input())
while test>0 :
	string = input()
	sum = 0
	for i in range(len(string)) :
		sum = sum + giai_thua(int(string[i]))
		if(sum>int(string)):
			break
	if sum == int(string): print("Yes")
	else : print("No")
	test -= 1
