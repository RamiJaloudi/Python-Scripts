import sys
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="I LOVE SHAIMAA !!!",fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="I LOVE SHAIMAA !!!", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="I LOVE SHAIMAA !!!", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="I LOVE SHAIMAA !!!", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()
