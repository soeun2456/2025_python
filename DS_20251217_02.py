from tkinter import*
def draw_shape():
    canvas.delete("all")
    choice=shape_var.get()

    if choice==1:
        canvas.create_rectangle(50,50,150,150, fill="red")
    elif choice==2:
        canvas.create_oval(200,80,300,180,fill="blue")
    elif choice==3:
        canvas.create_picture(200,200,200,200)

root=Tk()
root.title("중간고사 7번")
root.geometry("420x440")

canvas=Canvas(root, width=400, height=320, bg="white")
canvas.pack()

shape_var = IntVar()
shape_var.set(1)

frame=Frame(root)
frame.pack(pady=10)

button1=Button(root, text="사각형",padx=10)
button1.pack(side="left")
button2=Button(root, text="원",side="left",padx=10)
button3=Button(root, text="그림", side="left",padx=10)
button4=Button(root, text="지우기", command=reset)


result_label=Label(root,text="버튼을 눌러 도형을 선택하세요")

root.mainloop()
