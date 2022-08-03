from tkinter import *
window=Tk()
window.geometry("400x700")
window.title("Calculator")

def clicked(num):
    first_num=txt1.get()
    txt1.delete(0,END)
    txt1.insert(0,str(first_num)+str(num))
def add():
    first_number=txt1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="add"
    txt1.delete(0,END)
def minus():
    first_number=txt1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="minus"
    txt1.delete(0,END)
def mul():
    first_number=txt1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="mul"
    txt1.delete(0,END)
def div():
    first_number=txt1.get()
    global old_value
    old_value=int(first_number)
    global math
    math="div"
    txt1.delete(0,END)
def equal():
    if math=="add":
        new_value=txt1.get()
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)+int(new_value))
    if math=="minus":
        new_value=txt1.get()
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)-int(new_value))
    if math=="mul":
        new_value=txt1.get()
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)*int(new_value))
    if math=="div":
        new_value=txt1.get()
        txt1.delete(0,END)
        txt1.insert(0,int(old_value)/int(new_value))

l1=Label(window,text="-----",font=('Source Sans Pro Semibold',18))
txt1=Entry(window,font=('Source Sans Pro Semibold',25))
l3=Label(window,text="",font=('Source Sans Pro Semibold',40))


b5=Button(window,text="%",height=4,width=10)
b6=Button(window,text="CE",height=4,width=10)
b7=Button(window,text="C",height=4,width=10)
b8=Button(window,text="/",height=4,width=10,command=div)
b9=Button(window,text="7",height=4,width=10,command=lambda:clicked(7))
b10=Button(window,text="8",height=4,width=10,command=lambda:clicked(8))
b11=Button(window,text="9",height=4,width=10,command=lambda:clicked(9))
b12=Button(window,text="*",height=4,width=10,command=mul)
b13=Button(window,text="4",height=4,width=10,command=lambda:clicked(4))
b14=Button(window,text="5",height=4,width=10,command=lambda:clicked(5))
b15=Button(window,text="6",height=4,width=10,command=lambda:clicked(6))
b16=Button(window,text="-",height=4,width=10,command=minus)
b17=Button(window,text="1",height=4,width=10,command=lambda:clicked(1))
b18=Button(window,text="2",height=4,width=10,command=lambda:clicked(2))
b19=Button(window,text="3",height=4,width=10,command=lambda:clicked(3))
b20=Button(window,text="+",height=4,width=10,command=add)
b21=Button(window,text="+/-",height=4,width=10)
b22=Button(window,text="0",height=4,width=10,command=lambda:clicked(0))
b23=Button(window,text=".",height=4,width=10,command=lambda:clicked('.'))
b24=Button(window,text="=",height=4,width=10,bg="sky blue",command=equal)

l1.grid(row=0,column=0)
txt1.grid(row=2,column=4)
l3.grid(row=3,column=0)


b5.grid(row=6,column=0)
b6.grid(row=6,column=1)
b7.grid(row=6,column=2)
b8.grid(row=6,column=3)
b9.grid(row=7,column=0)
b10.grid(row=7,column=1)
b11.grid(row=7,column=2)
b12.grid(row=7,column=3)
b13.grid(row=8,column=0)
b14.grid(row=8,column=1)
b15.grid(row=8,column=2)
b16.grid(row=8,column=3)
b17.grid(row=9,column=0)
b18.grid(row=9,column=1)
b19.grid(row=9,column=2)
b20.grid(row=9,column=3)
b21.grid(row=10,column=0)
b22.grid(row=10,column=1)
b23.grid(row=10,column=2)
b24.grid(row=10,column=3)

window.mainloop()