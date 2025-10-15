#8-31 과 비슷

from tkinter import*

root=Tk()
root.geometry("300x100")

f=Frame(root)

button1=Button(f, text="버튼 1", bg="red", fg="white")
button2=Button(f, text="버튼 2", bg="green", fg="black")
button3=Button(f, text="버튼 3", bg="gray", fg="white")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

l=Label(root, text="이 레이블은 버튼들 위에 배치된다")
l.pack()
f.pack()

root.mainloop()