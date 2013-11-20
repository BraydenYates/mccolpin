from Tkinter import *

root = Tk()
#Title, duh. Look at the line!
root.title("Passion Project")

#Other Variables

photo = PhotoImage(file="accel.gif")
img = Label(root, image=photo)
img.photo = photo




    
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
#Introduction
var.set("My passion is coding. Someday, I'd love to get a job developing software or being an indie game developer. \n The question, however, is how can I align this with physics? ")


#Functions 
def acceleration():
    var.set("Acceleration \n \n \n \n \n \n Acceleration is defined as: \n 'the increase in the rate or speed of something. \n How could this be used in code? \n \n \n'")
    img.pack()
    var.set(" \n Image from https://share.ehs.uen.org/node/7931 \n \n \n ")

def newton():
  var.set("Newton's Laws \n \n \n")
    var.set("")
    

#Acceleration Button!
accel = Button(root, text='Acceleration', command=lambda: acceleration)
accel.pack()

#Newton's Button
newton = Button(root, text="Newton's Laws", command=newton)
newton.pack()

label.pack()
root.mainloop()
