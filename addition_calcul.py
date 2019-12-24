try:
    from Tkinter import *
except ImportError:
    from tkinter import *
     
def addition():
    firstnumber = int(one.get())
    secondnumber = int(two.get())
    answer = (firstnumber + secondnumber)
    answerdisplay = Label(text=answer)
    answerdisplay.pack()
 
master = Tk()
master.geometry("300x300")
master.title("SimpleCalculator")
one = Entry(width="40")
onelabel = Label(text="First Number")
onelabel.pack()
one.pack()
two = Entry(width="40")
twolabel = Label(text="Second Number")
twolabel.pack()
two.pack()
add = Button(text="Add", command=addition)
add.pack()
master.mainloop()
