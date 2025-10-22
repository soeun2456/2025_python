from tkinter import*

root=Tk()
message='''가나다라'''
w1=Label(root,padx=30, text=message).pack(side='right')

message='''삶이 그대를 속일지라도
슬퍼하지마라!'''
w2=Label(root,padx=10, text=message).pack(side='left')
root.mainloop()