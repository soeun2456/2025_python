'''문제 1. 은행 계좌(Account) 입출금 관리 프로그램
학습 포인트: 클래스 변수 관리(잔액), 조건문(출금 시 잔액 확인)

1. 클래스 구조

BankAccount 클래스

생성자에서 예금주 이름(owner)과 초기 잔액(balance, 기본값 0)을 설정한다.

deposit(amount): 잔액에 금액을 더하고 "입금 완료" 문자열 반환.

withdraw(amount): 잔액보다 금액이 크면 "잔액 부족", 아니면 차감 후 "출금 완료" 반환.

get_balance(): 현재 잔액 정보를 문자열로 반환.

2. 파일 처리

save_transaction(message): "bank_log.txt"에 거래 내역을 추가한다.

3. UI 동작

예금주 입력, 금액 입력 Entry 2개 존재.

[입금], [출금], [잔액확인] 버튼 구현.

각 버튼 클릭 시 해당 기능을 수행하고 결과를 라벨에 표시 및 파일에 기록'''


from tkinter import *

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"[{self.owner}] {amount}원 입금 완료. 잔액: {self.balance}원"

    def withdraw(self, amount):
        if amount > self.balance:
            return f"[{self.owner}] 출금 실패 (잔액 부족). 현재 잔액: {self.balance}원"
        self.balance -= amount
        return f"[{self.owner}] {amount}원 출금 완료. 잔액: {self.balance}원"

def save_transaction(message):
    with open("bank_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

# 전역 계좌 객체 (단순화를 위해 하나만 사용)
my_account = BankAccount("홍길동", 10000)

def click_deposit():
    try:
        amt = int(amt_entry.get())
        msg = my_account.deposit(amt)
        save_transaction(msg)
        res_label.config(text=msg)
    except ValueError:
        res_label.config(text="숫자를 입력하세요.")

def click_withdraw():
    try:
        amt = int(amt_entry.get())
        msg = my_account.withdraw(amt)
        save_transaction(msg)
        res_label.config(text=msg)
    except ValueError:
        res_label.config(text="숫자를 입력하세요.")

root = Tk()
root.title("문제1 - 은행")
root.geometry("350x250")

Label(root, text="금액 입력:").pack()
amt_entry = Entry(root)
amt_entry.pack()

res_label = Label(root, text=f"현재 잔액: {my_account.balance}원")
res_label.pack(pady=10)

Button(root, text="입금", command=click_deposit).pack(pady=2)
Button(root, text="출금", command=click_withdraw).pack(pady=2)

root.mainloop()