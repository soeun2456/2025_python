'''문제 3. 호텔 예약 시스템 (숙박비 계산)
특징: 날짜(숫자)와 요금(클래스 속성)의 곱셈 연산 + 조식 옵션 처리

클래스 설계

Room: 기본 요금 속성.

StandardRoom: 1박 8만원.

SuiteRoom: 1박 20만원.

GUI 구성

Entry: 숙박 일수(숫자) 입력.

Radiobutton: 스탠다드 / 스위트 룸 선택.

Checkbutton: "조식 포함 (1박당 1만원 추가)".

계산: (방 가격 + 조식 여부) * 숙박 일수.'''

import tkinter as tk

class Room:
    def __init__(self, price, name):
        self.price = price
        self.name = name

class StandardRoom(Room):
    def __init__(self):
        super().__init__(80000, "스탠다드룸")

class SuiteRoom(Room):
    def __init__(self):
        super().__init__(200000, "스위트룸")

def calculate():
    try:
        days = int(ent_days.get())
        room = StandardRoom() if var_room.get() == 1 else SuiteRoom()
        
        daily_price = room.price
        if var_breakfast.get():
            daily_price += 10000 # 조식비 추가
            
        total = daily_price * days
        
        lbl_info.config(text=f"객실: {room.name}\n기간: {days}박\n조식: {'포함' if var_breakfast.get() else '미포함'}\n총 결제액: {total:,}원")
        
    except ValueError:
        lbl_info.config(text="숙박 일수에 숫자를 입력하세요.")

root = tk.Tk()
root.title("문제 3 - 호텔 예약")
root.geometry("300x300")

tk.Label(root, text="숙박 일수 입력:").pack()
ent_days = tk.Entry(root)
ent_days.pack()

var_room = tk.IntVar(value=1)
tk.Radiobutton(root, text="스탠다드 (8만원)", variable=var_room, value=1).pack()
tk.Radiobutton(root, text="스위트 (20만원)", variable=var_room, value=2).pack()

var_breakfast = tk.IntVar()
tk.Checkbutton(root, text="조식 포함 (박당 1만원)", variable=var_breakfast).pack()

tk.Button(root, text="견적 내기", command=calculate).pack(pady=10)
lbl_info = tk.Label(root, text="결과창", bg="lightgray", width=30, height=5)
lbl_info.pack()

root.mainloop()