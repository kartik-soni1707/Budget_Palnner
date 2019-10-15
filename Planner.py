from tkinter import *
import tkinter.messagebox
def click():
    if variable.get()=='Select month' or name.get()=='' or int(spend.get())<0 :
        a1.delete(0,END)
        b1.delete(0,END)
        variable.set('Select month')
        tkinter.messagebox.showinfo('Alert Mesage','Invalid Details!!')
    else:
        pass
mn=Tk()
spend=StringVar()
name=StringVar()
variable=StringVar()
variable.set('Select month')
spend.set('')
mn.geometry('400x130+120+120')
mn.title("Welcome to Budget Planner")
a=Label(mn,text="Enter Name:",bg="red",fg="white",font="Times 15")
b=Label(mn,text="Enter Month:",bg="blue",fg="white",font="Times 15")
c=Label(mn,text="Enter Budget:",bg="green",fg="white",font="Times 15")
d=Button(mn,text="Submit",command=click,bg="black",fg="red",font="Times 15")
w = OptionMenu(mn, variable,'January','February','March','April','May','June','July','August','September','October','November','December')
w.grid(row=1,column=1,sticky=E)
a1 = Entry(mn,textvariable=name,font="Times 15")
b1 = Entry(mn,textvariable=spend,font="Times 15")
a.grid(row = 0,column = 0,sticky=W)
b.grid(row = 1,column = 0,sticky=W)
c.grid(row = 2,column = 0,sticky=W)
d.grid(row = 3,column = 1,sticky=W)
a1.grid(row = 0,column = 1)
b1.grid(row = 2,column = 1)


