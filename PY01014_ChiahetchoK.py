string = input()
list1 = string.split(" ")
a = int(list1[0])
k = int(list1[1])
n = int(list1[2])
if a >= n :
	print("-1")
else:
	begin = a//k + int(1)
	end = n//k
	if begin*k>n:
		print("-1")
	for i in range(begin,end+1,1):
		print((k*i-a),end = " ")
