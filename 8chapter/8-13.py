from tkinter import*

def button_clicked():
    print('버튼이클릭됨')

root=Tk()
root.geometry('700x700')

button=Button(root,text='클릭하세요',command=button_clicked())
button.pack()

root.mainloop()