from tkinter import *
window=Tk()
window.title("Application")
window.geometry("350x500")
window.configure(background="sky blue")
def click1():
    print("Button1 Clicked")
def click2():
    print("Button2 Clicked")
def click3():
    print("Button3 Clicked")
button1=Button(window,text="Button1",fg="red",bg="#f9ff9f",height=2,width=10, command=click1)
button2=Button(window,text="Button2",fg="red",bg="#f9ff9f",height=2,width=10, command=click2)
button3=Button(window,text="Button3",fg="red",bg="#f9ff9f",height=2,width=10, command=click3)
button1.pack()
button2.pack()
button3.pack()
window.mainloop() 