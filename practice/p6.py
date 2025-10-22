class BankAccount:
    def __init__(self,name,number,balance):
        self.name=name
        self.numbet=number
        self.balance=balance

    def balance(self):
        self.balance=0

    def deposit(self,amount): #입금
        self.balance+=amount
        print('입금 성공')

    def withdraw(self,amount): #출금
        if self.balance>=amount:
            self.balance-=amount
            print('인출 성공')

        else:
            print('잔액부족')

        

account=BankAccount('Kim','123456789',1000)
print('초기 잔고:', account.balance)

account.deposit(500)
print('저축 후 잔고:', account.balance)

account.withdraw(200)
print('인출 후 잔고:', account.balance)

account.withdraw(1500) #잔액부족