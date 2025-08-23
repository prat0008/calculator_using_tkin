from tkinter import *

x = Tk()
x.geometry("400x300")
x.title("CALC BY PRATEEK GOEL")

t = StringVar()
first_numb = 0
current_operator = ""

# calc output screen
display_entry = Entry(textvariable=t, width=35, borderwidth=5, font=('Arial', 12), justify='right')
display_entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

def click_number(number):
    current = t.get()
    if current == "0" or current in ["+", "-", "*", "/"]:
        t.set(str(number))
    else:
        t.set(current + str(number))

def click_operator(operator):
    global first_numb, current_operator
    try:
        first_numb = float(t.get())
        current_operator = operator
        t.set(operator)
    except:
        t.set("Error")

def click_equal():
    global first_numb, current_operator
    try:
        second_numb = float(t.get())
        
        if current_operator == "+":
            result = first_numb + second_numb
        elif current_operator == "-":
            result = first_numb - second_numb
        elif current_operator == "*":
            result = first_numb * second_numb
        elif current_operator == "/":
            if second_numb == 0:
                t.set("Error: Div by 0")
                return
            result = first_numb / second_numb
        else:
            t.set("Error")
            return
            
        t.set(str(result))
        first_numb = result
        current_operator = ""
    except:
        t.set("Error")

def clear():
    global first_numb, current_operator
    t.set("")
    first_numb = 0
    current_operator = ""

# Number buttons
b7 = Button(text="7", command=lambda: click_number(7), padx=5, pady=5, height=1, width=7)
b7.grid(row=1, column=0)

b8 = Button(text="8", command=lambda: click_number(8), padx=5, pady=5, height=1, width=7)
b8.grid(row=1, column=1)

b9 = Button(text="9", command=lambda: click_number(9), padx=5, pady=5, height=1, width=7)
b9.grid(row=1, column=2)

b4 = Button(text="4", command=lambda: click_number(4), padx=5, pady=5, height=1, width=7)
b4.grid(row=2, column=0)

b5 = Button(text="5", command=lambda: click_number(5), padx=5, pady=5, height=1, width=7)
b5.grid(row=2, column=1)

b6 = Button(text="6", command=lambda: click_number(6), padx=5, pady=5, height=1, width=7)
b6.grid(row=2, column=2)

b1 = Button(text="1", command=lambda: click_number(1), padx=5, pady=5, height=1, width=7)
b1.grid(row=3, column=0)

b2 = Button(text="2", command=lambda: click_number(2), padx=5, pady=5, height=1, width=7)
b2.grid(row=3, column=1)

b3 = Button(text="3", command=lambda: click_number(3), padx=5, pady=5, height=1, width=7)
b3.grid(row=3, column=2)

b0 = Button(text="0", command=lambda: click_number(0), padx=5, pady=5, height=1, width=7)
b0.grid(row=4, column=1)

# Operator buttons
o1 = Button(text="+", command=lambda: click_operator("+"), padx=5, pady=5, height=1, width=7)
o1.grid(row=1, column=3)

o2 = Button(text="-", command=lambda: click_operator("-"), padx=5, pady=5, height=1, width=7)
o2.grid(row=2, column=3)

o3 = Button(text="*", command=lambda: click_operator("*"), padx=5, pady=5, height=1, width=7)
o3.grid(row=3, column=3)

o4 = Button(text="/", command=lambda: click_operator("/"), padx=5, pady=5, height=1, width=7)
o4.grid(row=4, column=3)

# Equals button
e1 = Button(text="=", command=click_equal, padx=5, pady=5, height=1, width=7)
e1.grid(row=4, column=2)

# Clear button
c1 = Button(text="CLR", command=clear, padx=5, pady=5, height=1, width=7)
c1.grid(row=4, column=0)

x.mainloop()