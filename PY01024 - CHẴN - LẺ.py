test = int(input())
from math import*
while test>0:
	string = input()
	sum = 0
	kq =1
	for i in range(len(string)-1):
		sum += int(string[i])
		if abs(int(string[i])-int(string[i+1])) != 2:
			kq=0
	sum += int(string[len(string)-1])
	if kq == 1 and sum % 10 ==0:
		print("YES")
	else: print("NO")
	test -= 1
