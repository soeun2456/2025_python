class Employee:
    empCount=0 #클래스변수

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        Employee.empCount+=1 #클래스변수 값 변경
    
    def displayEmp(self):
        print(f'Name: {self.name}, Salary: {self.salary}')

emp1=Employee('Kim',5000)
emp2=Employee('Lee',6000)

emp1.displayEmp()
emp2.displayEmp()

print(f'Total employees: {Employee.empCount}')

    