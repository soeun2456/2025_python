class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getInfo(self):
        return (self.name, self.id)

best = Student('이수민', 101)

name, student_id = best.getInfo() 

print(f"학생 이름: {name}")
print(f"학생 ID: {student_id}")
