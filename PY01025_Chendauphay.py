string = input()
res = ""
dem = 0
for i in range(len(string)-1,-1,-1):
    if dem!=0 and dem%3==0:
        res = "," + res
    dem += 1
    res = string[i] + res
print(res)