from asyncio.windows_events import NULL
from logging import NullHandler


test = int(input())
for i in range(test):
    string = input()
    numberStr = string.split(" ")
    stringinput = input()
    strOne = ""
    strTwo=""
    list1 = stringinput.split(" ")
    if len(list1)==1:
        strOne += str(list[0])
        strTwo = input()
    else:
        strOne += str(list1[0])
        strTwo += str(list1[1])
    if int(numberStr[0]) > int(numberStr[1]):
        numberStr[0] , numberStr[1] = numberStr[1] , numberStr[0]
    resTwo = int(strOne.replace("numberStr[0]", "numberStr[1]")) + int(strTwo.replace("numberStr[0]", "numberStr[1]"))
    resOne = int(strOne.replace("numberStr[1]", "numberStr[0]")) + int(strTwo.replace("numberStr[1]", "numberStr[0]"))
    print(resOne+" "+ resTwo)