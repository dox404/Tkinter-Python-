from tkinter import *
win=Tk()
win.title("Chek Button")
win.geometry("300x300")
#radio button

radio=Radiobutton(win,text="male",value=0).pack()
radio=Radiobutton(win,text="female",value=1).pack()
radio=Radiobutton(win,text="other",value=2).pack()
#chek button
# chek=Checkbutton(win,text='male').place(x=250,y=250)
win.mainloop()