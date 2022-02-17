from tkinter import *
from tkinter.messagebox import *

#functions
def all_clear():
    textfield.delete(0,END)

def clear():
    x=textfield.get()
    x=x[0:len(x)-1]
    textfield.delete(0,END)
    textfield.insert(0,x)


def click_btn(event):
    print("button clicked")
    b=event.widget
    text=b["text"]
    print(text)
    
    
    if text=='=':
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
        except Exception as e:
            print("error",e)
            showerror("Error",e)


    textfield.insert(END,text)



win=Tk()
win.title("Calculator")
# win.maxsize(600,600)
win.geometry('300x300')
#textfeild
textfield=Entry(win,justify=LEFT,font=('',20))
textfield.pack(side=TOP,fil=X,padx=10)

buttonFrame=Frame(win)
buttonFrame.pack(side=TOP)

#adding Buttons
# btn1=Button(buttonFrame,text="1")
# btn1.grid(row=0,column= 0)
# btn2=Button(buttonFrame,text='2')
# btn2.grid(row='0',column='2')

temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),width=5,relief='ridge',activebackground='orange',activeforeground='white')
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp=temp+1
        btn.bind('<Button-1>',click_btn)

btn0=Button(buttonFrame,text='0',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btn0.grid(row=3,column=0,padx=5,pady=5)
btndot=Button(buttonFrame,text='.',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btndot.grid(row=3,column=1,padx=5,pady=5)
btnE=Button(buttonFrame,text='*',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnE.grid(row=3,column=2,padx=5,pady=5)
btnplus=Button(buttonFrame,text='+',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnplus.grid(row=0,column=3,padx=5,pady=5)
btndevi=Button(buttonFrame,text='/',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btndevi.grid(row=1,column=3,padx=5,pady=5)
btnminus=Button(buttonFrame,text='-',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnminus.grid(row=2,column=3,padx=5,pady=5)
btnmulti=Button(buttonFrame,text='=',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnmulti.grid(row=3,column=3,padx=5,pady=5)
btncl=Button(buttonFrame,text='<--',width=5,relief='ridge',activebackground='orange',activeforeground='white',command=clear)
btncl.grid(row=4,column=0,padx=5,pady=5)
btnacl=Button(buttonFrame,text='C',width=5,relief='ridge',activebackground='orange',activeforeground='white',command=all_clear)
btnacl.grid(row=4,column=1,padx=5,pady=5)

#bind
btn0.bind('<Button-1>',click_btn)
btndot.bind('<Button-1>',click_btn)
btnplus.bind('<Button-1>',click_btn)
btndevi.bind('<Button-1>',click_btn)
btnminus.bind('<Button-1>',click_btn)
btnmulti.bind('<Button-1>',click_btn)
btnE.bind('<Button-1>',click_btn)

# scintific function


scframe=Frame(win)
btnsqrt=Button(scframe,text='sqrt',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnsqrt.grid(row=0,column=0,padx=5,pady=5)
btnpower=Button(scframe,text='power',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnpower.grid(row=0,column=1,padx=5,pady=5)
btnfactorial=Button(scframe,text='!',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnfactorial.grid(row=0,column=2,padx=5,pady=5)
btnrad=Button(scframe,text='rad',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnrad.grid(row=0,column=3,padx=5,pady=5)
btnsin=Button(scframe,text='sin',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btnsin.grid(row=1,column=0,padx=5,pady=5)
btncos=Button(scframe,text='cos',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btncos.grid(row=1,column=1,padx=5,pady=5)
btntan=Button(scframe,text='tan',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btntan.grid(row=1,column=2,padx=5,pady=5)
btndegree=Button(scframe,text='degree',width=5,relief='ridge',activebackground='orange',activeforeground='white')
btndegree.grid(row=1,column=3,padx=5,pady=5)



normalCalculator=True
    
def sc_cal(event):
    print("btn...")


def sc_click():
    global normalCalculator
    print("clicked")
    if normalCalculator:
        buttonFrame.pack_forget()
        scframe.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        print("show Scintific")
        normalCalculator=False
      
    else:
        print("show normal")
        scframe.pack_forget()
        normalCalculator=True

btnsqrt.bind("<-Button->",sc_cal)


menubar=Menu(win)
Mode=Menu(menubar,tearoff=0)
Mode.add_checkbutton(label="Scintific calculator",command=sc_click)
menubar.add_cascade(label="Mode",menu=Mode)
win.config(menu=menubar)


win.mainloop()