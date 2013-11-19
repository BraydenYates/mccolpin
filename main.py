#from Tkinter import *

#master = Tk()

#def callback():
#    print "click!"

#b = Button(master, text="OK", command=callback)
#b.pack()

#mainloop()

from Tkinter import *

root = Tk()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("My passion is coding. Someday, I'd love to get a job developing software or being an indie game developer. \n The question, however, is how can I align this with physics? ")

def one():
    var.set("Acceleration \n \n \n Here is information on how acceleration is implemented into coding.")

b = Button(root, text="Continue", command=one)
b.pack()


label.pack()
root.mainloop()
