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
        
        two = tk.Label(master, text="Acceleration \n \n \n ")
        two.pack()
        
        self.master.title("Acceleration")
        
        #https://share.ehs.uen.org/node/7931
        
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
        
        two = tk.Label(master, text="Momentum \n \n \n  Momentum is 'The quantity of motion of a moving body.' \n In coding, anything that moves has momentum. Most game engines allow you to give other objects mass. \n Mass is required for momentum, so any time anything moves in a game, it has momentum.")
        
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























def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
