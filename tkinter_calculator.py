from tkinter import *

sign = ""
total = 0

root = Tk()
root.title("Calculator Pro")

def num_insert(num):
    screen.insert(END, num)
    
def add():
    global total
    global sign
    sign="+"
    total = screen.get()
    screen.delete(0, END)

def sub():
    global total
    global sign
    sign="-"
    total = screen.get()
    screen.delete(0, END)

def mul():
    global total
    global sign
    sign="*"
    total = screen.get()
    screen.delete(0, END)

def div():
    global total
    global sign
    sign="/"
    total = screen.get()
    screen.delete(0, END)

def equal():
    num2 = screen.get()
    global sign
    global total
    total =int(total)
    num2 =int(num2)
    if sign == "+":
        total += num2
    elif sign == "-":
        total -= num2
    elif sign == "*":
        total *= num2
    elif sign == "/":
        total /= num2
    screen.delete(0, END)
    screen.insert(END, total)


def clear():
    screen.delete(0, END)
    global sign
    global total
    sign = ""
    total = 0

screen = Entry(root, width=35) 
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10,)

button7 = Button(root, text="7", padx=20, pady=10, command=lambda:num_insert(7))
button8 = Button(root, text="8", padx=20, pady=10, command=lambda:num_insert(8))
button9 = Button(root, text="9", padx=20, pady=10, command=lambda:num_insert(9))
button_div= Button(root, text="/", padx=19, pady=10, command=div)

button4 = Button(root, text="4", padx=20, pady=10, command=lambda:num_insert(4))
button5 = Button(root, text="5", padx=20, pady=10, command=lambda:num_insert(5))
button6 = Button(root, text="6", padx=20, pady=10, command=lambda:num_insert(6))
button_mul= Button(root, text="*", padx=19, pady=10, command=mul)

button1 = Button(root, text="1", padx=20, pady=10, command=lambda:num_insert(1))
button2 = Button(root, text="2", padx=20, pady=10, command=lambda:num_insert(2))
button3 = Button(root, text="3", padx=20, pady=10, command=lambda:num_insert(3))
button_sub= Button(root, text="-", padx=19, pady=10, command=sub)

button_clear = Button(root, text="C", padx=19, pady=10, command=clear)
button0 = Button(root, text="0", padx=20, pady=10, command=lambda:num_insert(0))
button_equal= Button(root, text="=", padx=19, pady=10, command=equal)
button_add= Button(root, text="+", padx=17, pady=10, command=add)


button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_div.grid(row= 1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_mul.grid(row= 2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_sub.grid(row= 3, column=3)

button_clear.grid(row= 4, column=0)
button0.grid(row=4, column=1)
button_equal.grid(row= 4, column=2)
button_add.grid(row= 4, column=3)

root.mainloop()