#from Tkinter import *

#master = Tk()

#def callback():
#    print "click!"

#b = Button(master, text="OK", command=callback)
#b.pack()

#mainloop()

from Tkinter import *

root = Tk()
#Title, duh. Look at the line!
root.title("Passion Project")

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
#Introduction
var.set("My passion is coding. Someday, I'd love to get a job developing software or being an indie game developer. \n The question, however, is how can I align this with physics? ")
#Functions 
def acceleration():
    var.set("Acceleration \n \n \n \n \n \n Acceleration is defined as: \n 'the increase in the rate or speed of something. \n How could this be used in code? \n \n \n'")


b1 = Button(root, text="Acceleration", command=acceleration)
b1.pack()


label.pack()
root.mainloop()
