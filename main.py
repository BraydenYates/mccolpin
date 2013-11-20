from Tkinter import *

root = Tk()
#Title, duh. Look at the line!
root.title("Passion Project")

#Other Variables

photo = PhotoImage(file="accel.gif")
img = Label(root, image=photo)
img.photo = photo

#http://www.batesville.k12.in.us/physics/phynet/mechanics/momentum/Images/elephant_momentum.gif - Link for image, to upload.
phototwo = PhotoImage(file:"elephant_momentum.gif")
imgtwo = Label(root, image=phototwo)
imgtwo.photo = imgtwo.phototwo



    
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
#Introduction
var.set("My passion is coding. Someday, I'd love to get a job developing software or being an indie game developer. \n The question, however, is how can I align this with physics? ")


#Functions 
def acceleration():
    var.set("Acceleration \n \n \n \n \n \n Acceleration is defined as: \n 'the increase in the rate or speed of something.' \n How could this be used in code? \n \n \n")
    var.set("\n \n \n Acceleration can be used in coding during game development. In game development, things may need to change their speed/velocity. ")
    img.pack()
    var.set(" \n Image from https://share.ehs.uen.org/node/7931 \n \n \n ")

def newton():
  var.set("Newton's Laws \n \n \n")
    var.set("")
    

def moment():
    var.set("Momentum \n \n \n \n \n \n")
    var.set("Momentum  is the movement of a mass. How could momentum be used in coding?\n \n \n \n ")
    var.set("In coding, momentum can be used whenever an object moves. \n")
    var.set("Most games have something that you move away from, your movement and the other gameobject's movement use \n")
    var.set("momentum in a virtual enviornment.")
    
    imgtwo.pack()
    var.set("\n \n \n \n \n \n Image from: \n http://www.batesville.k12.in.us/physics/phynet/mechanics/momentum/Images/elephant_momentum.gif")
    
#Acceleration Button!
accel = Button(root, text='Acceleration', command=lambda: acceleration)
accel.pack()

#Newton's Button
newton = Button(root, text="Newton's Laws", command=newton)
newton.pack()

moment = Button(root, text='Momentum', command=:lambda: moment)
moment.pack()

label.pack()
root.mainloop()
