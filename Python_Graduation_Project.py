from tkinter import *
import random
import time
import datetime

window = Tk()
window.geometry("1500x5000")
window.title("Cafe Shop Management System")
window.resizable(FALSE, FALSE)
Label(text="Cafe Shop Management System", bg="black", fg="white", font=("calibri", 33), width="300", height="3").pack()

#=========================================================================

Tea = StringVar()
Mocha = StringVar()
Iced_Mocha = StringVar()
Latte = StringVar()
Iced_Latte = StringVar()
Coffee = StringVar()
Ice_Coffee = StringVar()
Hot_Chocolate = StringVar()
Caramel_Macchiato = StringVar()
Americano = StringVar()
Cost = StringVar()
Tax = StringVar()
Total_Cost = StringVar()

#=========================================================================

def Reset():
     entry_Tea.delete(0, END)
     entry_Mocha.delete(0, END)
     entry_Iced_Mocha.delete(0, END)
     entry_Coffee.delete(0, END)
     entry_Ice_Coffee.delete(0, END)
     entry_Iced_Latte.delete(0, END)
     entry_Caramel_Macchiato.delete(0, END)
     entry_Hot_Chocolate.delete(0, END)
     entry_Latte.delete(0, END)
     entry_Americano.delete(0, END)

def Sub():
     try: a1 = int(Tea.get())
     except: a1 = 0

     try: a2 = int(Coffee.get())
     except: a2 = 0

     try: a3 = int(Caramel_Macchiato.get())
     except: a3 = 0

     try: a4 = int(Ice_Coffee.get())
     except: a4 = 0

     try: a5 = int(Iced_Latte.get())
     except: a5 = 0

     try: a6 = int(Iced_Mocha.get())
     except: a6 = 0

     try: a7 = int(Americano.get())
     except: a7 = 0

     try: a8 = int(Latte.get())
     except: a8 = 0

     try: a9 = int(Mocha.get())
     except: a9 = 0

     try: a10 = int(Hot_Chocolate.get())
     except: a10 = 0

     c1 = a1*2
     c2 = a2*1.75
     c3 = a3*4.35
     c4 = a4*2.25
     c5 = a5*3.75
     c6 = a6*4.25
     c7 = a7*2.10
     c8 = a8*2.8
     c9 = a9*3.3
     c10 = a10*4

     lbl_Cost = Label(f3, font=('Gabriola', 20, 'bold'), text=" Cost", width=15, fg="black", bg="Gray")
     lbl_Cost.grid(row=1, column=0)
     entry_Cost = Entry(f3, font=('Gabriola', 20, 'bold'), textvariable=Cost, bd=6, width=20, bg="white")
     entry_Cost.grid(row=1, column=1)

     lbl_Tax = Label(f3, font=('Gabriola', 20, 'bold'), text="Tax", width=15, fg="black", bg="Gray")
     lbl_Tax.grid(row=2, column=0)
     entry_Tax = Entry(f3, font=('Gabriola', 20, 'bold'), textvariable=Tax, bd=6, width=20, bg="white")
     entry_Tax.grid(row=2, column=1)

     lbl_Total_Cost = Label(f3, font=('Gabriola', 20, 'bold'), text="Total Cost", width=15, fg="black", bg="Gray")
     lbl_Total_Cost.grid(row=3, column=0)
     entry_Total_Cost = Entry(f3, font=('Gabriola', 20, 'bold'), textvariable=Total_Cost, bd=6, width=20, bg="white")
     entry_Total_Cost.grid(row=3, column=1)

     Cost = "Rs", str('%.2f' % (c1 + c2 + c3 + c4 + c5 + c6 +c7 + c8 + c9 + c10 ))
     PayTax = ((c1 + c2 + c3 + c4 + c5 + c6 +c7 + c8 + c9 + c10 ) * 0.2)
     OverAllCost = "Rs", str('%.2f' % (PayTax + Cost ))

     Cost.set(PayTax)
     Tax.set(PayTax)
     Total_Cost.set(OverAllCost)

def qExit():
    window.destroy()


#=========================================================================

f1 = Frame(window, bg="pink", highlightbackground="black", highlightthickness=1, width=500, height=580)
f1.pack(padx=250, pady=250)
f1.place(x=30, y=190)

Label(f1, text="Menu", font=("Gabriola", 40, "bold"), fg="black", bg="pink").place(x=200, y=20)
Label(f1, text="Tea....2$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=80)
Label(f1, text="Mocha....3.3$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=130)
Label(f1, text="Iced Mocha....4.25$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=180)
Label(f1, text="Latte....2.8$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=230)
Label(f1, text="Iced Latte....3.75$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=280)
Label(f1, text="Coffee....1.75$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=330)
Label(f1, text="Ice Coffee....2.25$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=380)
Label(f1, text="Hot Chocolate....4$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=430)
Label(f1, text="Caramel Macchiato....4.35$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=480)
Label(f1, text="Americano....2.10$", font=("Lucida Calligraphy", 20, "bold"), fg="black", bg="pink").place(x=20, y=530)
#=========================================================================

f3 = Frame(window, highlightbackground="black", highlightthickness=1, width=700, height=1000)
f3.pack()
f3.place(x=1100, y=200)

#=========================================================================

f2 = Frame(window, bg="Gray", highlightbackground="black", highlightthickness=1, width=500, height=40)
f2.pack()
f2.place(x=530, y=190)

lbl_Tea = Label(f2, font=('arial', 20, 'bold'), text="Tea", width=10, fg="white", bg="Gray")
lbl_Tea.grid(row=1, column=0)
entry_Tea = Entry(f2, font=('arial', 20, 'bold'), textvariable=Tea, bd=6, width=20, bg="white")
entry_Tea.grid(row=1, column=1)

lbl_Mocha = Label(f2, font=('arial', 20, 'bold'), text="Mocha", width=15, fg="white", bg="Gray")
lbl_Mocha.grid(row=2, column=0)
entry_Mocha = Entry(f2, font=('arial', 20, 'bold'), textvariable=Mocha, bd=6, width=20, bg="white")
entry_Mocha.grid(row=2, column=1)

lbl_Iced_Mocha = Label(f2, font=('arial', 20, 'bold'), text="Iced Mocha", width=15, fg="white", bg="Gray")
lbl_Iced_Mocha.grid(row=3, column=0)
entry_Iced_Mocha = Entry(f2, font=('arial', 20, 'bold'), textvariable=Iced_Mocha, bd=6, width=20, bg="white")
entry_Iced_Mocha.grid(row=3, column=1)

lbl_Latte = Label(f2, font=('arial', 20, 'bold'), text="Latte", width=15, fg="white", bg="Gray")
lbl_Latte.grid(row=4, column=0)
entry_Latte = Entry(f2, font=('arial', 20, 'bold'), textvariable=Latte, bd=6, width=20, bg="white")
entry_Latte.grid(row=4, column=1)

lbl_Iced_Latte = Label(f2, font=('arial', 20, 'bold'), text="Iced Latte", width=15, fg="white", bg="Gray")
lbl_Iced_Latte.grid(row=5, column=0)
entry_Iced_Latte = Entry(f2, font=('arial', 20, 'bold'), textvariable=Iced_Latte, bd=6, width=20, bg="white")
entry_Iced_Latte.grid(row=5, column=1)

lbl_Coffee = Label(f2, font=('arial', 20, 'bold'), text="Coffee", width=15, fg="white", bg="Gray")
lbl_Coffee.grid(row=6, column=0)
entry_Coffee = Entry(f2, font=('arial', 20, 'bold'), textvariable=Coffee, bd=6, width=20, bg="white")
entry_Coffee.grid(row=6, column=1)

lbl_Ice_Coffee = Label(f2, font=('arial', 20, 'bold'), text="Ice Coffee", width=15, fg="white", bg="Gray")
lbl_Ice_Coffee.grid(row=7, column=0)
entry_Ice_Coffee = Entry(f2, font=('arial', 20, 'bold'), textvariable=Ice_Coffee, bd=6, width=20, bg="white")
entry_Ice_Coffee.grid(row=7, column=1)

lbl_Hot_Chocolate = Label(f2, font=('arial', 20, 'bold'), text="Hot Chocolate", width=15, fg="white", bg="Gray")
lbl_Hot_Chocolate.grid(row=8, column=0)
entry_Hot_Chocolate = Entry(f2, font=('arial', 20, 'bold'), textvariable=Hot_Chocolate, bd=6, width=20, bg="white")
entry_Hot_Chocolate.grid(row=8, column=1)

lbl_Caramel_Macchiato = Label(f2, font=('arial', 20, 'bold'), text="Caramel Macchiato", width=15, fg="white", bg="Gray")
lbl_Caramel_Macchiato.grid(row=9, column=0)
entry_Caramel_Macchiato = Entry(f2, font=('arial', 20, 'bold'), textvariable=Caramel_Macchiato, bd=6, width=20, bg="white")
entry_Caramel_Macchiato.grid(row=9, column=1)

lbl_Americano = Label(f2, font=('arial', 20, 'bold'), text="Americano", width=10, fg="white", bg="Gray")
lbl_Americano.grid(row=10, column=0)
entry_Americano = Entry(f2, font=('arial', 20, 'bold'), textvariable=Americano, bd=6, width=20, bg="white")
entry_Americano.grid(row=10, column=1)


#=========================================================================

btnTotal=Button(f3,padx=10,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="PaleVioletRed3",command=Sub).grid(row=10,column=4)

btnReset=Button(f3,padx=10,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="PaleVioletRed3",command=Reset).grid(row=11,column=4)

btnExit=Button(f3,padx=10,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="PaleVioletRed3",command=qExit).grid(row=12,column=4)

#=========================================================================



window.mainloop()


