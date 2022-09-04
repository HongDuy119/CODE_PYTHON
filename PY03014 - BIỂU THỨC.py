from inspect import stack


for i in range(int(input())):
    s = input()
    st = stack()
    dem = 1
    for j in s:
        if j =='(':
            print(dem,end = " ")
            st.append(dem)
            dem += 1
        if j == ')':
            k = st.pop()
            print(k,end=" ")
    print()
    