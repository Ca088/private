class class1:
    __pvar=50
    def __method(self):
        print("Its inside private private")
    def function1(self):
        print("Private variable:",class1.__pvar)

obj=class1()
obj.function1()
obj.__method()#error

class computer:
    def __init__(self):
        self.__max=50000
    def sell(self):
        print("Price",self.__max)
    def setmax(self,price):
        self.__max=price
c=computer()
c.sell()
c.__max=70000
c.sell()
c.setmax(80000)
c.sell()

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
p1=Point(2,3)
print(p1)
