from tkinter import*
from tkinter.messagebox import showinfo
root=Tk()
root.geometry("300x200")
root.title("Checkbot Demo")

agree=StringVar()

agree.set("비동의")

def event_prac():
    showinfo(title="결과", message=agree.get())

Checkbutton(root, 
    text="동의합니다.",
    command=event_prac,
    variable=agree,
    onvalue="동의",
    offvalue="비동의").pack()

root.mainloop()