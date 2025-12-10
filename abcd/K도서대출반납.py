'''문제 5. 도서관(Library) 대출/반납 시스템
학습 포인트: 상태 메시지 처리, 간단한 문자열 조작

1. 클래스 구조

Book(title): 책 제목 저장.

EBook(Book): borrow() -> "[E-Book] {제목} 다운로드 완료" 반환.

PaperBook(Book): borrow() -> "[종이책] {제목} 대출 데스크에서 수령하세요" 반환.

2. 파일 처리

record_history(msg): "library_history.txt"에 기록.

clear_history(): 기록 삭제.

3. UI 동작

책 제목 입력 Entry.

[전자책 대출], [종이책 대출] 버튼.

[기록 삭제] 버튼.

비어있는 입력값 처리("제목없음").'''

from tkinter import *

class Book:
    def __init__(self, title):
        self.title = title
    def borrow(self):
        return f"{self.title} 대출 처리 중..."

class EBook(Book):
    def borrow(self):
        return f"[E-Book] '{self.title}' 다운로드 링크 생성 완료."

class PaperBook(Book):
    def borrow(self):
        return f"[종이책] '{self.title}' 서가 위치: A-12 확인 요망."

def record_history(msg):
    with open("library_history.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def clear_history():
    with open("library_history.txt", "w", encoding="utf-8") as f:
        pass
    lbl_status.config(text="대출 기록 삭제됨.")

def get_title():
    t = ent_title.get().strip()
    return t if t else "무제"

def borrow_ebook():
    title = get_title()
    b = EBook(title)
    msg = b.borrow()
    record_history(msg)
    lbl_status.config(text=msg)

def borrow_paper():
    title = get_title()
    b = PaperBook(title)
    msg = b.borrow()
    record_history(msg)
    lbl_status.config(text=msg)

root = Tk()
root.title("문제5 - 도서관")
root.geometry("350x250")

Label(root, text="도서 제목:").pack(pady=5)
ent_title = Entry(root, width=30)
ent_title.pack()

lbl_status = Label(root, text="대출 결과가 표시됩니다.", fg="blue")
lbl_status.pack(pady=15)

frame = Frame(root)
frame.pack()

Button(frame, text="전자책 대출", command=borrow_ebook).pack(side=LEFT, padx=5)
Button(frame, text="종이책 대출", command=borrow_paper).pack(side=LEFT, padx=5)
Button(root, text="기록 삭제", command=clear_history).pack(pady=10)

root.mainloop()