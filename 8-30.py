from tkinter import*

root=Tk()
root.geometry("300x100")

button1=Button(root, text="버튼 1", bg="red", fg="white")
button2=Button(root, text="버튼 2", bg="green", fg="black")
button3=Button(root, text="버튼 3", bg="gray", fg="white")
button1.pack()
button2.pack()
button3.pack()

root.mainloop()