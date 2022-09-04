class Thi_sinh:
    sum =0
    def __init__(self,name,age,mark1,mark2,mark3):
        self.name = name
        self.age = age
        self.make1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.sum = mark1+mark2+mark3
    def inn(self):
        print(self.name,self.age,"{:.1f}".format(self.sum))
if __name__ =='__main__':
    name = input()
    age = input()
    mark1 = float(input())
    mark2 = float(input())
    mark3 = float(input())
    TS = Thi_sinh(name,age,mark1,mark2,mark3)
    TS.inn()