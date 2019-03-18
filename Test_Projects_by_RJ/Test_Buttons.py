import sys
from tkinter import *

def clear():
    txtDisplay.delete(0, END)
    return

root = Tk()
frame = Frame(root)
frame.pack()

root.title('Calculator')
num1=StringVar()

topframe = Frame(root)
topframe.pack( side = TOP)

txtDisplay=Entry (frame, textvariable = num1, bd = 20, insertwidth = 1, font = 30)
txtDisplay.pack( side = TOP)

button1 = Button (topframe, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button1.pack(side =LEFT)

button2 = Button (topframe, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button2.pack(side =LEFT)

button3 = Button (topframe, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button3.pack(side =LEFT)

button4 = Button (topframe, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button4.pack(side =LEFT)


frame1 = Frame(root)
frame1.pack( side = TOP)

button1 = Button (frame1, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button1.pack(side =LEFT)

button2 = Button (frame1, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button2.pack(side =LEFT)

button3 = Button (frame1, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button3.pack(side =LEFT)

button3 = Button (frame1, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button3.pack(side =LEFT)


frame2 = Frame(root)
frame2.pack( side = TOP)

button1 = Button (frame2, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button1.pack(side =LEFT)

button2 = Button (frame2, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button2.pack(side =LEFT)

button3 = Button (frame2, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black", command=clear)
button3.pack(side =LEFT)

button4 = Button (frame2, padx=16, pady=16, bd=8, text="I Love Shaimaa!!!", fg="black")
button4.pack(side =LEFT)


frame4 = Frame(root)
frame4.pack( side = TOP)

button1 = Button (frame4, padx=16, pady=16, bd=8, text="*", fg="black")
button1.pack(side =LEFT)

button2 = Button (frame4, padx=16, pady=16, bd=8, text="/", fg="black")
button2.pack(side =LEFT)

button3 = Button (frame4, padx=16, pady=16, bd=8, text="-", fg="black")
button3.pack(side =LEFT)

button4 = Button (frame4, padx=16, pady=16, bd=8, text="+", fg="black")
button4.pack(side =LEFT)

root.mainloop()
