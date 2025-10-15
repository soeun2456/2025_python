from tkinter import*

def key_press(Event):
    print("키가 눌렸습니다:", event.keysym)

root=Tk()
root.geometry("200x200")

root.bind("<Key>", key_press)
root.focus_set()

root.mainloop()