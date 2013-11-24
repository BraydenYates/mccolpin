import Tkinter as tk
from Tkinter import *

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #START TITLE
        self.master.title("Start Menu")
        #TEXT
        one = tk.Label(master, text="My passion is coding. Some day I'd like to get a career as a software developer \n or a indie game developer.")
        one.pack()
        #NEW WINDOW BUTTON
        self.button1 = tk.Button(self.frame, text = 'Next', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        #NEW WINDOW FUNCTION
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Acceleration \n \n \n Acceleration is defined as 'the increase in the rate of something. \n' In computing, this can be used in racing games. When a car begins to move, it is accelerating. \n When the car is slowing down, it is accelerating")
        two.pack()
        
        self.master.title("Acceleration")
        
        #https://share.ehs.uen.org/node/7931
        cite = tk.Label(master, text="https://share.ehs.uen.org, . Acceleration in Cars. 2013. Photograph. \n https://share.ehs.uen.org/node/7931Web. 23 Nov 2013. \n <http://media.ehs.uen.org/html/PhysicsQ2/Direction_01/acc2.jpg>. ")
        cite.pack()
        photo = PhotoImage(file="accel.gif")
        img = Label(master, image=photo)
        img.photo = photo

        img.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo3(self.newWindow)


class Demo3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Speed \n \n \n Speed is, by definition, 'How far something goes in a given amount of time.' \n \n \n How is this involved in coding? /n Lets say you're developing a racing game. In order to win, you must logically go the given distance \n in less time than the other players, or NPC's. ")
        
        two.pack()
        
        self.master.title("Speed")
        #http://www.regentsprep.org/regents/physics/phys01/velocity/default.htm
        phototwo = PhotoImage(file="speed.gif")
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()

        cite = tk.Label(master, text="Wagon, Joy. Ladybugs and Speed. 1999. Photograph. \n http://www.regentsprep.org/regents/physics/phys01/velocity/default.htm Web. 23 Nov 2013. \n <http://www.regentsprep.org/regents/physics/phys01/velocity/distdisp.gif>.")
        cite.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo4(self.newWindow)

class Demo4:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Momentum \n \n \n Momentum is 'The quantity of motion of a moving body.' \n In coding, anything that moves has momentum. Most game engines allow you to give other objects mass. \n Mass is required for momentum, so any time anything moves in a game, it has momentum.")
        
        two.pack()
        
        self.master.title("Momentum")
        #http://www.batesville.k12.in.us/physics/phynet/mechanics/momentum/Images/elephant_momentum.gif
        phototwo = PhotoImage(file="elephant_momentum.gif")

        three = tk.Label(master, text="Stanbrough, . Momentum of an elephant. 2013.\n Graphic. http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm \n Web. 20 Nov 2013. <http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm>.")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo5(self.newWindow)


class Demo5:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Potential Energy \n \n \n Potential energy is energy that has the ability to be released, but has not yet been excerted. \n An example of this in coding is when your machine is off. When your machine \n is off, no power is running in it, but you have power stored in a battery that has the ability to be excerted when you \n press the power button. ")
        
        two.pack()
        
        self.master.title("Potential Energy")
        #http://static.ddmcdn.com/gif/power-supply5.jpg && http://computer.howstuffworks.com/power-supply.htm
        phototwo = PhotoImage(file="psu.gif")

        three = tk.Label(master, text=" Garry Brown . Power Supply Unit. 2001. \n Photograph. http://computer.howstuffworks.com/power-supply.htmWeb. 23 Nov 2013. \n <http://static.ddmcdn.com/gif/power-supply5.jpg>. ")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo6(self.newWindow)


class Demo6:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Kinetic Energy \n \n \n Kinetic Energy is energy that has been exerted.\n In computers, kinetic energy is used in hardware to make the computer run. \n When you press the power button, the potential energy is exerted through the computer to power it, making it kinetic energy")
        
        two.pack()
        
        self.master.title("Kinetic Energy")
        #http://static.ddmcdn.com/gif/power-supply5.jpg && http://computer.howstuffworks.com/power-supply.htm
        phototwo = PhotoImage(file="psu.gif")

        three = tk.Label(master, text="Stanbrough, . Momentum of an elephant. 2013.\n Graphic. http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm \n Web. 20 Nov 2013. <http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm>.")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo7(self.newWindow)


class Demo7:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Newton's 1st Law \n \n \n Newton's First Law states that: \n 'an object at rest tends to stay at rest, while an object in motion tends to stay in motion. \n' In computing, this law can be shown by the fan in your PC. \n The fan does not move unless it is given energy to make it move. If there is no energy to power the fan, \n it will stop moving due to an unbalanced force (friction). \n If you were in an environment in which there was no gravity or friction, your fan would continue to move forever. ")
        
        two.pack()
        
        self.master.title("Newton's First Law")
        #http://teachertech.rice.edu/Participants/louviere/Newton/law1.html
        phototwo = PhotoImage(file="first.gif")

        three = tk.Label(master, text="Stanbrough, . Momentum of an elephant. 2013.\n Graphic. http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm \n Web. 20 Nov 2013. <http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm>.")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo8(self.newWindow)


class Demo8:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Newton's 2nd Law \n \n \n Newton's Second Law states that: \n 'Acceleration is produced when when a force acts on a mass. \n' In computing, this law can be represented by hardware required to run a program. \n Some lightweight programs (less mass) can use older, slower hardware (Less force). \n Most modern games (more mass) , however, require \n powerful hardware. (More force) ")
        
        two.pack()
        
        self.master.title("Newton's 2nd Law")
        #http://teachertech.rice.edu/Participants/louviere/Newton/law1.html
        phototwo = PhotoImage(file="first.gif")

        three = tk.Label(master, text="Stanbrough, . Momentum of an elephant. 2013.\n Graphic. http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm \n Web. 20 Nov 2013. <http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm>.")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo9(self.newWindow)

class Demo9:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Newton's 3rd Law \n \n \n Third Law states that: \n 'For every action, there is an equal and opposite reaction.' \n This can be relative to coding, whenever you fix a bug, (the action) The bug is solved and 312 more are made for \n you to solve. ")
        
        two.pack()
        
        self.master.title("Newton's Third Law")
        #http://teachertech.rice.edu/Participants/louviere/Newton/law1.html
        phototwo = PhotoImage(file="third.gif")

        three = tk.Label(master, text="Nasa & LTP, . Third Law of Motion Applied to Boat. \n 2013. Graphic. http://www.allstar.fiu.edu/aero/rocket1.htmWeb. \n 23 Nov 2013. \n <http://www.allstar.fiu.edu/aero/images/pic007.gif>. ")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo10(self.newWindow)




class Demo10:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
        two = tk.Label(master, text="Citations")
        two.pack()
        
        self.master.title("Citations")
        #http://teachertech.rice.edu/Participants/louviere/Newton/law1.html
        phototwo = PhotoImage(file="first.gif")

        three = tk.Label(master, text="Stanbrough, . Momentum of an elephant. 2013.\n Graphic. http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm \n Web. 20 Nov 2013. <http://www.batesville.k12.in.us/physics/phynet/Mechanics/Momentum/momentum.htm>.")
        three.pack()
        
        imgtwo = Label(master, image=phototwo)
        imgtwo.photo = phototwo

        imgtwo.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        #cont = tk.Button(self.frame, text = 'Continue', command = self.new_window)
        #cont.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

    #def new_window(self):
        #self.newWindow = tk.Toplevel(self.master)
        #self.app = Demo1(self.newWindow)


# DO NOT TOUCH

def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
