from tkinter import *
window=Tk()
window.geometry("500x700")
def add():
    text.set(int(txt1.get())+int(txt2.get()))
def sub():
    text.set(int(txt1.get())-int(txt2.get()))
def mul():
    text.set(int(txt1.get())*int(txt2.get()))
def div():
    text.set(int(txt1.get())/int(txt2.get()))
text=StringVar()
txt1=Entry()
txt2=Entry()
button1=Button(window,text="+",width=17,command=add)
button2=Button(window,text="-",width=16,command=sub)
button3=Button(window,text=" ",width=15,command=mul)
button4=Button(window,text="Division",width=15,command=div)
txt3=Entry(textvariable=text)
txt1.grid(row=0)
txt2.grid(row=0,column=1)
button1.grid(row=2,column=0)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
button4.grid(row=2,column=3)
txt3.grid(row=3)
window.mainloop()