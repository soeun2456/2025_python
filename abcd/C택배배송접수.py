'''문제 4. 택배 배송 접수 (무게 및 운송 수단)
특징: 운송 수단에 따른 배송 예정일(메시지) 변경과 파손 주의 옵션

클래스 설계

Delivery: get_time() 메서드 (자식에서 구현).

RegularDelivery: "3~4일 소요".

ExpressDelivery: "익일 도착".

GUI 구성

Entry: 받는 사람 이름.

Radiobutton: 일반 택배 / 특급 택배.

Checkbutton: "파손 주의 스티커", "문 앞 배송 요청".

출력: 받는 사람, 배송 예상 시간, 요청 사항 표시.'''

import tkinter as tk

class Delivery:
    def get_time(self): return ""

class RegularDelivery(Delivery):
    def get_time(self): return "3~4일 소요 (일반)"

class ExpressDelivery(Delivery):
    def get_time(self): return "내일 도착 (특급)"

def submit():
    name = ent_receiver.get() or "고객"
    method = ExpressDelivery() if var_type.get() == 2 else RegularDelivery()
    
    notes = []
    if var_fragile.get(): notes.append("파손주의")
    if var_door.get(): notes.append("문앞배송")
    note_str = " / ".join(notes) if notes else "없음"
    
    result = f"받는 분: {name}\n배송 타입: {method.get_time()}\n요청 사항: {note_str}"
    lbl_confirm.config(text=result)

root = tk.Tk()
root.title("문제 4 - 택배 접수")
root.geometry("300x300")

tk.Label(root, text="받는 사람:").pack()
ent_receiver = tk.Entry(root)
ent_receiver.pack()

var_type = tk.IntVar(value=1)
tk.Radiobutton(root, text="일반 택배", variable=var_type, value=1).pack()
tk.Radiobutton(root, text="특급 택배 (빠름)", variable=var_type, value=2).pack()

var_fragile = tk.IntVar()
var_door = tk.IntVar()
tk.Checkbutton(root, text="파손 주의", variable=var_fragile).pack()
tk.Checkbutton(root, text="문 앞 배송", variable=var_door).pack()

tk.Button(root, text="접수하기", command=submit).pack(pady=10)
lbl_confirm = tk.Label(root, text="접수 대기", fg="blue")
lbl_confirm.pack()

root.mainloop()