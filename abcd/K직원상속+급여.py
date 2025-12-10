'''문제 2. 직원(Employee) 상속 + 급여 계산기
학습 포인트: 상속과 다형성 (직급별 급여 계산 로직 분리)

1. 상속 구조

Employee(name, base_pay): 기본 급여 계산 (base_pay 반환).

Manager(Employee): calculate_pay() 오버라이딩 -> 기본급 + 보너스(기본급의 20%) 더한 값 반환.

PartTimer(Employee): calculate_pay() 오버라이딩 -> 기본급(시급) * 160(시간) 으로 계산하여 반환. (단순화)

2. 파일 처리

log_payroll(msg): "payroll.txt"에 급여 명세 저장.

3. UI 동작

이름과 기본급(또는 시급)을 입력받음.

[매니저 등록], [아르바이트 등록] 버튼.

버튼 클릭 시 해당 객체 생성 -> 급여 계산 -> 파일 저장 -> 라벨 출력.'''

from tkinter import *

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay
    
    def calculate_pay(self):
        return self.base_pay

class Manager(Employee):
    def calculate_pay(self):
        return int(self.base_pay * 1.2) # 보너스 20%

class PartTimer(Employee):
    def calculate_pay(self):
        return self.base_pay * 160 # 시급 * 160시간

def log_payroll(msg):
    with open("payroll.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def process_manager():
    name = name_entry.get()
    pay = int(pay_entry.get())
    m = Manager(name, pay)
    result = m.calculate_pay()
    msg = f"[매니저] {name} 최종 급여: {result}원"
    log_payroll(msg)
    lbl_result.config(text=msg)

def process_parttimer():
    name = name_entry.get()
    pay = int(pay_entry.get())
    p = PartTimer(name, pay)
    result = p.calculate_pay()
    msg = f"[알바] {name} (160시간 기준) 최종 급여: {result}원"
    log_payroll(msg)
    lbl_result.config(text=msg)

root = Tk()
root.title("문제2 - 급여계산")
root.geometry("300x300")

Label(root, text="이름:").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="기본급/시급:").pack()
pay_entry = Entry(root)
pay_entry.pack()

lbl_result = Label(root, text="결과 대기 중")
lbl_result.pack(pady=20)

Button(root, text="매니저 급여 계산", command=process_manager).pack()
Button(root, text="알바 급여 계산", command=process_parttimer).pack()

root.mainloop()