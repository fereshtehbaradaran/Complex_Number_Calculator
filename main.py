import math
from tkinter import *
from complexNumber import Complex
from operations import subtraction, summation, multiplication, division, power

expression = ""
 
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def makeComplex(string):
    real = 0
    i = 0
    while string[i] != "+" and string[i] != "-":
        real = real*10 + int(string[i])
        i += 1
    isNegative = True if string[i] == "-" else False
    i += 1
    img = 0
    while string[i] != "i":
        img = img*10 + int(string[i])
        i+= 1
    img = -1 * img if isNegative else 1 * img
    return Complex(real,img)
    
    
def expPress():
    global expression
    c = makeComplex(expression) 
    equation.set(c.exp())
    expression = ""

def rctPress():
    global expression
    c = makeComplex(expression) 
    equation.set(c.rct())
    expression = ""
 
def triPress():
    global expression
    c = makeComplex(expression) 
    equation.set(c.tri())
    expression = ""


def equalpress():
    try:
        global expression
        
        i = expression.index('i')
        
        first = makeComplex(expression[:i+1])
        opration = expression[i+1]
        
        if opration == "+":
            second = makeComplex(expression[i+2:])
            total = summation(first,second).rct()
            
        elif opration == "-":
            second = makeComplex(expression[i+2:])
            total = subtraction(first,second).rct()
            
        elif opration == "*":
            second = makeComplex(expression[i+2:])
            total = multiplication(first,second).rct()
            
        elif opration == "/":
            second = makeComplex(expression[i+2:])
            total = division(first,second).rct()
        
        elif opration == "^":
            second = int(expression[i+2:])
            total = power(first,second).rct()
        
        equation.set(total)
        expression = ""
 
    except:
 
        equation.set(" error ")
        expression = ""

 
 

if __name__ == "__main__":
    gui = Tk()
 
    gui.configure(background="gray30")
    gui.title("Complex Calculator")
    gui.geometry("325x205")
 
    equation = StringVar()
 
    expression_field = Entry(gui, textvariable=equation)
 
    expression_field.grid(columnspan=4, ipadx=80)
 
    button1 = Button(gui, text=' 1 ', fg='black', bg='thistle',
                    command=lambda: press(1), height=1, width=8)
    button1.grid(row=3, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='thistle',
                    command=lambda: press(2), height=1, width=8)
    button2.grid(row=3, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='thistle',
                    command=lambda: press(3), height=1, width=8)
    button3.grid(row=3, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='thistle',
                    command=lambda: press(4), height=1, width=8)
    button4.grid(row=4, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='thistle',
                    command=lambda: press(5), height=1, width=8)
    button5.grid(row=4, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='thistle',
                    command=lambda: press(6), height=1, width=8)
    button6.grid(row=4, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='thistle',
                    command=lambda: press(7), height=1, width=8)
    button7.grid(row=5, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='thistle',
                    command=lambda: press(8), height=1, width=8)
    button8.grid(row=5, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='thistle',
                    command=lambda: press(9), height=1, width=8)
    button9.grid(row=5, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='thistle',
                    command=lambda: press(0), height=1, width=8)
    button0.grid(row=6, column=1)
    
    buttoni = Button(gui, text=' i ', fg='black', bg='light gray',
                    command=lambda: press('i'), height=1, width=8)
    buttoni.grid(row=6, column=2)
 
    plus = Button(gui, text=' + ', fg='black', bg='light gray',
                command=lambda: press("+"), height=1, width=8)
    plus.grid(row=3, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='light gray',
                command=lambda: press("-"), height=1, width=8)
    minus.grid(row=4, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='light gray',
                    command=lambda: press("*"), height=1, width=8)
    multiply.grid(row=5, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='light gray',
                    command=lambda: press("/"), height=1, width=8)
    divide.grid(row=6, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='light gray',
                command=equalpress, height=1, width=8)
    equal.grid(row=6, column=0)
    
    power = Button(gui, text=' pow ', fg='black', bg='light gray',
                command=lambda: press("^"), height=1, width=8)
    power.grid(row=2, column=0)
    
    exp = Button(gui, text=' exp ', fg='black', bg='light gray',
                command=expPress, height=1, width=8)
    exp.grid(row=2, column=1)
    
    rct = Button(gui, text=' rct ', fg='black', bg='light gray',
                command=rctPress, height=1, width=8)
    rct.grid(row=2, column=2)
    
    tri = Button(gui, text=' tri ', fg='black', bg='light gray',
                command=triPress, height=1, width=8)
    tri.grid(row=2, column=3)
    
    gui.mainloop()