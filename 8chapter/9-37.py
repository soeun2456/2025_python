class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getage(self):
        return self.__age,self.__name

obj=Student('hong',20)
print(obj.getage())