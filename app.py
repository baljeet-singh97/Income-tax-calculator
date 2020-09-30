from tkinter import *
from tkinter import ttk

exp = " "
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)
    
def clear ():
    global exp
    exp = " "
    equation.set(" ")

def taxamount(income):
    totalamount=0
    tax=0
    if income <= 500000:
        tax = 0
        
    elif income <= 1000000:
        tax = 12500 + (income) * 0.20
        
    elif income >= 1000001:
        tax = 112500 + (income) * 0.30
    else:
        tax = 12500+100000+(income - 1000000)* 0.3
    
    totalamount=tax
    return totalamount

def butter():
    income=IntVar()
    income=incomefield.get()
    entryField.delete(0,'end')
    amount = taxamount(int(income))
    print(amount)
    entry.set(str(amount))
    


root=Tk() 



root.configure(background="lightgrey")
root.resizable(0,0)
root.geometry('300x280')
root.title("income Tax Calculator")

entry= StringVar()
equation = StringVar()

# *************************************************************************
inputField = Frame(root)
inputField.place(x=20,y=10)

labelincome = Label(inputField,text="Your Income",background="royalblue",width=12,foreground="White")
labelincome.grid(row=0, column=0)
incomefield = Entry(inputField,textvariable = equation, width = 20,background="SkyBlue2",foreground="black",justify=CENTER)
incomefield.grid(row=0,column=1)


totaltax = Label(inputField,text="Total Tax",background="royalblue",width=12,foreground="white")
totaltax.grid(row=1,column=0)
entryField = Entry(inputField,textvariable = entry, width = 20,background="Yellowgreen",foreground="black",justify=CENTER)
entryField.grid(row=1,column=1)

# *************************************************************************
findTaxFrame = Frame(root)
findTaxFrame.place(x=20,y=80)

button = Button(findTaxFrame,text="Find Income Tax", width = 30,activebackground="cyan",background='skyblue', command=butter)
button.grid(row=2,column=0,columnspan=3)

# *************************************************************************
numpadFrame = Frame(root)
numpadFrame.place(x=20,y=120)

btn9 = ttk.Button(numpadFrame, text = '9' , width = 10 ,  command = lambda : press(9) )
btn9.grid(row=0,column=0)

btn8 = ttk.Button(numpadFrame, text = '8' , width = 10 ,  command = lambda : press(8) )
btn8.grid(row=0,column=1)

btn7 = ttk.Button(numpadFrame, text = '7' , width = 10 ,  command = lambda : press(7) )
btn7.grid(row=0,column=2)

btn6 = ttk.Button(numpadFrame, text = '6' , width = 10 ,  command = lambda : press(6) )
btn6.grid(row=1,column=0)

btn5 = ttk.Button(numpadFrame, text = '5' , width = 10 ,  command = lambda : press(5) )
btn5.grid(row=1,column=1)

btn4 = ttk.Button(numpadFrame, text = '4' , width = 10 ,  command = lambda : press(4) )
btn4.grid(row=1,column=2)

btn3 = ttk.Button(numpadFrame, text = '3' , width = 10,  command = lambda : press(3)  )
btn3.grid(row=2,column=0)

btn2 = ttk.Button(numpadFrame, text = '2' , width = 10, command = lambda : press(2)  )
btn2.grid(row=2,column=1)

btn1 = ttk.Button(numpadFrame, text = '1' , width = 10 ,  command = lambda : press(1) )
btn1.grid(row=2,column=2)

zeroAndClearFrame = Frame(root)
zeroAndClearFrame.place(x=20,y=220)

btn0= ttk.Button(zeroAndClearFrame, text = '0' , width = 10,  command = lambda : press(0)  )
btn0.grid(row=3,column=0)

btnclr = Button(zeroAndClearFrame, text = 'Clear' , width = 19, background='orange', activebackground='red',activeforeground='white',  command = clear )
btnclr.grid(row=3,column=1)

root.mainloop()