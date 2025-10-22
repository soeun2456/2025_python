class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        self.__balance -= amount
        print(amount, '출금됨')
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(amount, '입금됨')
        return self.__balance

    # ▼▼▼ 잔액 확인 메소드 추가 ▼▼▼
    def get_balance(self):
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(10)

print("남아있는 금액:", a.get_balance())