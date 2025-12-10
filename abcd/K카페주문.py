'''문제 3. 카페 메뉴 주문(Order) 시스템
학습 포인트: 객체 속성 활용, 문자열 포맷팅, 파일 초기화

1. 클래스 구조

Beverage(name, price): 음료 이름과 가격 저장.

Coffee(Beverage): order() 메서드 -> "{이름} 커피 주문 접수 (가격: {가격}원)" 반환.

Juice(Beverage): order() 메서드 -> "{이름} 주스 주문 접수 (가격: {가격}원) - 얼음 컵 제공" 반환.

2. 파일 처리

save_order(msg): "orders.txt"에 주문 저장.

reset_orders(): 파일 내용 삭제.

3. UI 동작

메뉴 이름 입력 Entry.

[커피 주문], [주스 주문] 버튼 -> 각각 Coffee, Juice 객체 생성(가격은 임의 지정) 후 처리.

[주문 내역 초기화] 버튼 -> 파일 비우기.'''

from tkinter import *

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def order(self):
        return f"{self.name} 주문: {self.price}원"

class Coffee(Beverage):
    def order(self):
        return f"[Coffee] {self.name} 준비됨 ({self.price}원)"

class Juice(Beverage):
    def order(self):
        return f"[Juice] {self.name} + 얼음컵 제공 ({self.price}원)"

def save_order(msg):
    with open("orders.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def reset_orders():
    with open("orders.txt", "w", encoding="utf-8") as f:
        pass
    lbl_res.config(text="주문 내역이 초기화되었습니다.")

def order_coffee():
    name = entry_menu.get()
    c = Coffee(name, 3000) # 가격 고정
    msg = c.order()
    save_order(msg)
    lbl_res.config(text=msg)

def order_juice():
    name = entry_menu.get()
    j = Juice(name, 4500) # 가격 고정
    msg = j.order()
    save_order(msg)
    lbl_res.config(text=msg)

root = Tk()
root.title("문제3 - 카페")
root.geometry("300x250")

Label(root, text="메뉴 이름 입력:").pack(pady=5)
entry_menu = Entry(root)
entry_menu.pack(pady=5)

lbl_res = Label(root, text="주문 결과")
lbl_res.pack(pady=10)

Button(root, text="커피 주문(3000원)", command=order_coffee).pack()
Button(root, text="주스 주문(4500원)", command=order_juice).pack()
Button(root, text="주문 내역 초기화", command=reset_orders).pack(pady=5)

root.mainloop()