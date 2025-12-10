'''문제 4. 도형(Shape) 면적 기록 프로그램학습 포인트: 수학적 계산 로직, 입력값 검증(Validation)

1. 상속 구조Shape: area() 메서드 (NotImplementedError).Circle(radius): area() -> 원의 넓이 계산 ($3.14 \times r^2$).

    반환값은 문자열 "원 넓이: xx.xx".Square(side): area() -> 정사각형 넓이 계산 ($side \times side$).

    반환값은 문자열 "정사각형 넓이: xx".

2. 파일 처리log_area(result): "geometry_log.txt"에 결과 저장.

3. UI 동작입력 칸 하나(반지름 또는 한 변의 길이).

    [원 넓이 저장], [정사각형 넓이 저장] 버튼.결과를 소수점 둘째 자리까지 라벨에 표시.

'''

from tkinter import *

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        val = 3.14 * self.r * self.r
        return f"반지름 {self.r}인 원의 넓이: {val:.2f}"

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self):
        val = self.s * self.s
        return f"변의 길이 {self.s}인 정사각형 넓이: {val}"

def log_area(msg):
    with open("geometry_log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def calc_circle():
    try:
        val = float(ent_num.get())
        c = Circle(val)
        msg = c.area()
        log_area(msg)
        lbl_show.config(text=msg)
    except ValueError:
        lbl_show.config(text="숫자를 입력하세요")

def calc_square():
    try:
        val = float(ent_num.get())
        s = Square(val)
        msg = s.area()
        log_area(msg)
        lbl_show.config(text=msg)
    except ValueError:
        lbl_show.config(text="숫자를 입력하세요")

root = Tk()
root.title("문제4 - 도형")
root.geometry("300x200")

Label(root, text="길이(반지름/변) 입력:").pack()
ent_num = Entry(root)
ent_num.pack()

lbl_show = Label(root, text="계산 결과")
lbl_show.pack(pady=10)

Button(root, text="원 넓이 저장", command=calc_circle).pack()
Button(root, text="정사각형 넓이 저장", command=calc_square).pack()

root.mainloop()