from tkinter import *
x=Tk()
x.geometry("600x600")
x.title("CALC BY PRATEEK GOEL")

#calc ouput screen
t=StringVar()
cur_pos=" "


t.set("")
display_entry = Entry(textvariable=t,width=35, borderwidth=5) #font=('Arial', 24), bd=5, insertwidth=4, bg="lightgray", justify='right')
display_entry.grid(row=0,column=0,columnspan=4,padx=10, pady=10) 


def click_7():
        t.set(7)
def click_8():
        t.set(8)
def click_9():
        t.set(9)
def click_4():
        t.set(4)
def click_5():
        t.set(5)
def click_6():
        t.set(6)
def click_1():
        t.set(1)
def click_2():
        t.set(2)
def click_3():
        t.set(3)
def click_0():
        t.set(0) 

def click_plus():
        global first_numb
        first_numb = float(t.get())
        t.set("+")
def click_equal():
        second_numb =float(t.get())
        result=  first_numb + second_numb
        t.set(result)

def click_minus():
        global first_numb
        first_numb =float(t.get())
        t.set("-")


def click_multiply():
        global first_numb
        first_numb =float(t.get())
        t.set("*")


def click_divide():
        global first_numb
        first_numb =float(t.get())
        t.set("/")
def clear():
        t.set("")
                
        
#buttons command
b7=Button(text="7",command=click_7,padx=5,pady=5,height=1,width=7)
b7.grid(row=1, column=0)

b8=Button(text="8",command=click_8,padx=5,pady=5,height=1,width=7)
b8.grid(row=1, column=1)

b9=Button(text="9",command=click_9,padx=5,pady=5,height=1,width=7)
b9.grid(row=1, column=2)

b4=Button(text="4",command=click_4,padx=5,pady=5,height=1,width=7)
b4.grid(row=2, column=0)

b5=Button(text="5",command=click_5,padx=5,pady=5,height=1,width=7)
b5.grid(row=2, column=1)

b6=Button(text="6",command=click_6,padx=5,pady=5,height=1,width=7)
b6.grid(row=2, column=2)

b1=Button(text="1",command=click_1,padx=5,pady=5,height=1,width=7)
b1.grid(row=3, column=0)

b2=Button(text="2",command=click_2,padx=5,pady=5,height=1,width=7)
b2.grid(row=3, column=1)

b3=Button(text="3",command=click_3,padx=5,pady=5,height=1,width=7)
b3.grid(row=3, column=2)

b0=Button(text="0",command=click_0,padx=5,pady=5,height=1,width=7)
b0.grid(row=4, column=1)

#operators command
o1=Button(text="+",command=click_plus,padx=5,pady=5,height=1,width=7)
o1.grid(row=1, column=4)

o2=Button(text="-",command=click_minus,padx=5,pady=5,height=1,width=7)
o2.grid(row=2, column=4)

o3=Button(text="*",command=click_multiply,padx=5,pady=5,height=1,width=7)
o3.grid(row=3, column=4)

o4=Button(text="/",command=click_divide,padx=5,pady=5,height=1,width=7)
o4.grid(row=4, column=4)

#equals command
e1=Button(text="=",command=click_equal,padx=5,pady=5,height=1,width=7)
e1.grid(row=5, column=4)

#clear command
c1=Button(text="CLR",command=clear,padx=5,pady=5,height=1,width=7)
c1.grid(row=1, column=5)

x.mainloop()