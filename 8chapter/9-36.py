class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name,'is barking')

x=Dog('jack',3)
y=Dog('Daisy',5)

x.bark()
y.bark()
print(x.name,'is',x.age,'years old')
print(y.name,'is',y.age,'years old')