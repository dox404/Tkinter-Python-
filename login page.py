from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Login Page")
# win.iconbitmap("icon.ico")
win.minsize(500,500)
win.maxsize(600,600)
# win.geometry('300x300')
lbl=Label(win,text="Name",bg="black",fg="white",width=5,height=1)
lbl.place(x=150,y=100)
ent=Entry(win,bg="white")
ent.place(x=200,y=100)
lbl2=Label(win,text="Email",bg="black",fg="white",width=5,height=1)
lbl2.place(x=150,y=125)
ent2=Entry(win,bg='white')
ent2.place(x=200,y=125)
lbl3=Label(win,text="Mobile",bg='black',fg='white',width=5,height=1)
lbl3.place(x=150,y=150)
# #combobox
com=ttk.Combobox(win,width=3)
com['values']=(
    '+91',
    '+1',
    '+72'
)
com['state']='readonly'
com.place(x=200,y=150)

ent3=Entry(win,bg='white')
ent3.place(x=250,y=150)

btn=Button(win,text="Submit",bg="blue",fg="white")
btn.place(x=200,y=200)
win.mainloop()

