def tong(n):
    sum = 0
    for i in n:
        sum = sum + ord(i)- ord('0')
    return str(sum)
n = input()
dem = 0
while len(n)>1:
    # print(n)
    n = tong(n)
    dem += 1
print(dem)
