'''문제 2. 게임 캐릭터 생성기 (스탯 설정)
특징: 클래스별 기본 능력치(다형성)와 장비 장착(Checkbutton)에 따른 문자열 조합

클래스 설계

Character(name): attack() 메서드 보유.

Warrior(Character): attack() -> "대검 휘두르기!" (기본 힘 100).

Mage(Character): attack() -> "파이어볼 발사!" (기본 지능 100).

GUI 구성

Entry: 캐릭터 이름 입력.

Radiobutton: 전사 / 마법사 선택.

Checkbutton: "전설의 무기 장착", "방어구 강화".

결과: 선택한 직업의 공격 대사와 장착 아이템 목록 출력.'''

import tkinter as tk

class Character:
    def __init__(self, name):
        self.name = name
    def attack(self):
        return "공격!"

class Warrior(Character):
    def attack(self):
        return "강력한 대검 베기! (물리 데미지)"

class Mage(Character):
    def attack(self):
        return "거대 파이어볼 투척! (마법 데미지)"

def create_char():
    name = ent_name.get().strip() or "모험가"
    job = var_job.get()
    
    char = Warrior(name) if job == "warrior" else Mage(name)
    
    items = []
    if var_weapon.get(): items.append("전설의 무기")
    if var_armor.get(): items.append("강화 갑옷")
    
    item_str = ", ".join(items) if items else "맨손/맨몸"
    
    msg = f"[{name}] 캐릭터 생성 완료!\n직업: {'전사' if job=='warrior' else '마법사'}\n스킬: {char.attack()}\n장비: {item_str}"
    lbl_res.config(text=msg)

root = tk.Tk()
root.title("문제 2 - 캐릭터 생성")
root.geometry("300x300")

tk.Label(root, text="캐릭터 이름:").pack()
ent_name = tk.Entry(root)
ent_name.pack()

var_job = tk.StringVar(value="warrior")
tk.Radiobutton(root, text="전사 (Warrior)", variable=var_job, value="warrior").pack()
tk.Radiobutton(root, text="마법사 (Mage)", variable=var_job, value="mage").pack()

var_weapon = tk.IntVar()
var_armor = tk.IntVar()
tk.Checkbutton(root, text="전설의 무기 장착", variable=var_weapon).pack()
tk.Checkbutton(root, text="방어구 강화", variable=var_armor).pack()

tk.Button(root, text="생성하기", command=create_char).pack(pady=10)
lbl_res = tk.Label(root, text="대기 중...", fg="darkgreen")
lbl_res.pack()

root.mainloop()