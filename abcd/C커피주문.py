'''문제 5. 커피 주문 커스텀 (음료 제조)
특징: Person-Pet 관계처럼, Coffee 객체가 Option 정보를 포함하거나 속성을 변경

클래스 설계

Coffee: 기본 make() 메서드 ("커피 추출").

Americano(Coffee): make() -> "에스프레소 + 물".

Latte(Coffee): make() -> "에스프레소 + 우유".

GUI 구성

Radiobutton: 아메리카노 / 라떼.

Checkbutton: "샷 추가", "시럽 추가".

버튼: 제조하기 클릭 시, "주문하신 [메뉴] 나왔습니다. (옵션: ...)" 출력.'''

import tkinter as tk

class Coffee:
    def make(self): pass

class Americano(Coffee):
    def make(self): return "아메리카노 (물+에스프레소)"

class Latte(Coffee):
    def make(self): return "카페라떼 (우유+에스프레소)"

def brew():
    # 객체 생성 (다형성)
    coffee = Latte() if var_menu.get() == "latte" else Americano()
    
    # 옵션 문자열 처리
    add_ons = []
    if var_shot.get(): add_ons.append("샷 추가")
    if var_syrup.get(): add_ons.append("시럽 추가")
    
    add_on_msg = f"({', '.join(add_ons)})" if add_ons else "(기본)"
    
    lbl_out.config(text=f"주문하신 {coffee.make()} 나왔습니다.\n옵션: {add_on_msg}")

root = tk.Tk()
root.title("문제 5 - 카페")
root.geometry("300x250")

tk.Label(root, text="음료 선택").pack(pady=5)
var_menu = tk.StringVar(value="ame")
tk.Radiobutton(root, text="아메리카노", variable=var_menu, value="ame").pack()
tk.Radiobutton(root, text="카페라떼", variable=var_menu, value="latte").pack()

tk.Label(root, text="퍼스널 옵션").pack(pady=5)
var_shot = tk.IntVar()
var_syrup = tk.IntVar()
tk.Checkbutton(root, text="샷 추가", variable=var_shot).pack()
tk.Checkbutton(root, text="시럽 추가", variable=var_syrup).pack()

tk.Button(root, text="제조하기", command=brew, bg="brown", fg="white").pack(pady=10)
lbl_out = tk.Label(root, text="...", font=("돋움", 10))
lbl_out.pack()

root.mainloop()