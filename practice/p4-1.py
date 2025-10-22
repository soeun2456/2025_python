class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def info(self):
        print(f'{self.name}의 연봉은 {self.salary}입니다.')

    def raise_salary(self,amount):
        self.salary+=amount
        print(f'{self.name}의 연봉이 {self.salary}로 증가되었습니다.')
    

kim=Employee('Kim',5000)
lee=Employee('Lee',6000)

kim.info()
lee.info()

kim.raise_salary(2000)
lee.raise_salary(2000)


