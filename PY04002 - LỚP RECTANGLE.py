class Rectangle:
    def __init__(self,length,wide,color):
        self.length = length
        self.wide = wide
        self.color = color.lower().title()
    def check(self): 
        if self.length<=0 or self.wide<=0: return 1
        return 0
    def inn(self):
        if self.check() == 0: print((self.length + self.wide) * 2, self.wide * self.length, self.color, sep = ' ')
        else: print('INVALID')
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
r.inn()
