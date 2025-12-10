'''문제 1. 햄버거 키오스크 (가격 계산 시스템)
특징: 상속을 통한 가격 결정, Checkbutton을 이용한 추가 금액 합산

1.클래스 설계

Burger(name, price): 기본 버거 클래스.

CheeseBurger: 가격 5000원, desc() 호출 시 "치즈의 풍미" 반환.

ShrimpBurger: 가격 6000원, desc() 호출 시 "통새우의 식감" 반환.

2.GUI 구성

Radiobutton: 치즈버거(5000원) / 새우버거(6000원) 선택.

Checkbutton: 세트 업그레이드(+2000원), 감자튀김 라지 변경(+500원).

버튼: [주문하기] 클릭 시 총 결제 금액과 주문 내역 출력.'''

import tkinter as tk

class Burger:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def desc(self):
        return "맛있는 햄버거"

class CheeseBurger(Burger):
    def __init__(self):
        super().__init__("치즈버거", 5000)
    def desc(self):
        return "고소한 치즈의 풍미"

class ShrimpBurger(Burger):
    def __init__(self):
        super().__init__("새우버거", 6000)

    def desc(self):
        return "탱글한 통새우의 식감"

def order():
    # 1. 버거 객체 생성
    choice = var_burger.get()
    burger = CheeseBurger() if choice == 1 else ShrimpBurger()
    
    # 2. 옵션 비용 계산
    total_price = burger.price
    opts = []
    
    if var_set.get():
        total_price += 2000
        opts.append("세트(+2000)")
    if var_large.get():
        total_price += 500
        opts.append("라지 변경(+500)")
        
    opt_str = ", ".join(opts) if opts else "단품"
    
    # 3. 결과 출력
    msg = f"주문 메뉴: {burger.name}\n설명: {burger.desc()}\n옵션: {opt_str}\n\n총 금액: {total_price}원"
    lbl_result.config(text=msg)

root = tk.Tk()
root.title("문제 1 - 햄버거 키오스크")
root.geometry("300x350")

tk.Label(root, text="메뉴를 선택하세요", font=("Arial", 14)).pack(pady=10)

var_burger = tk.IntVar(value=1)
tk.Radiobutton(root, text="치즈버거 (5000원)", variable=var_burger, value=1).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="새우버거 (6000원)", variable=var_burger, value=2).pack(anchor="w", padx=20)

tk.Label(root, text="추가 옵션").pack(pady=5)
var_set = tk.IntVar()
var_large = tk.IntVar()
tk.Checkbutton(root, text="세트 업그레이드 (+2000원)", variable=var_set).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="감자튀김 라지 변경 (+500원)", variable=var_large).pack(anchor="w", padx=20)

tk.Button(root, text="주문하기", command=order, bg="orange").pack(pady=15)
lbl_result = tk.Label(root, text="결과가 여기에 표시됩니다.", justify="left", fg="blue")
lbl_result.pack()

root.mainloop()