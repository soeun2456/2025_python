from tkinter import*

root=Tk()
root.geometry("300x100")

button1=Button(root, text="버튼 1", bg="red", fg="white")
button2=Button(root, text="버튼 2", bg="green", fg="black")
button3=Button(root, text="버튼 3", bg="gray", fg="white")

button1.pack(side=LEFT,padx=10)
button2.pack(side=LEFT,padx=20)
button3.pack(side=LEFT)

root.mainloop()