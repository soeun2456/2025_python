class Cat:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def setname(self,name):
        self.__name=name

    def setage(self,age):
        self.__age=age

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age
    
m=Cat('missy',3)
l=Cat('lucky',5)
print(m.getname(),m.getage())
print(l.getname(),l.getage())
        