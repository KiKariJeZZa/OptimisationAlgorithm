#-----------------------------------------------
# GUI for an optimisation algorithm for a
# novel hybrid autonomous mining excavation
# system
#
# Author: Jeremiah Casuga
# ----------------------------------------------

from tkinter import Tk, Label, Button
import header
import energetic

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Optimisation Algorithm")

        self.label = Label(master, text="Optimisation Algorithm")
        self.label.pack()


    
root = Tk()
gui = GUI(root)
root.mainloop()