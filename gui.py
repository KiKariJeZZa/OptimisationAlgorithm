#-----------------------------------------------
# GUI for an optimisation algorithm for a
# novel hybrid autonomous mining excavation
# system
#
# Author: Jeremiah Casuga
# ----------------------------------------------

from tkinter import *
import header as header
import energetic as energetic
from functools import partial

class GUI:
    def __init__(self, master, energetics, headers):
        self.master = master
        master.title("Optimisation Algorithm")

        self.header = header.Header(headers)
        self.energetic = energetic.Energetics(energetics)

        self.master.label = Label(master, text="Optimisation Algorithm")
        self.master.label.config(font = ('Helvetica bold',30))
        self.master.label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        self.master.label.pack()

        self.name_energetic = StringVar()
        self.ROI_energetic = StringVar()

    def drop_menu(self):
        return 0

    def button(self):
        return 0

    

    def submit(self, master):
        energetic_name = self.name_energetic.get()
        energetic_roi = self.ROI_energetic.get()
        self.energetic.add_energetics([energetic_name,energetic_roi])
        print(self.energetic.get_energetics())
        master.destroy()
    
    def new_window_energetic(self):
        newWindow = Toplevel(self.master)
        newWindow.title("Enter new energetic")
        newWindow.geometry("300x100")

        submit_btn = Button(newWindow, text = 'Okay', command=partial(self.submit,newWindow))

        name_label = Label(newWindow, text = "Name")
        new_name = Entry(newWindow, textvariable=self.name_energetic)
        ROI_label = Label(newWindow, text = "ROI")
        new_ROI = Entry(newWindow, textvariable=self.ROI_energetic)
        name_label.grid(row=0,column=0)
        new_name.grid(row=0,column=1)
        ROI_label.grid(row=1,column=0)
        new_ROI.grid(row=1,column=1)
        submit_btn.grid(row=2,column=0)
    
    def refresh(self):
        self.destroy()
        self.__init__()



if __name__ == '__main__':
    root = Tk()
    root.geometry("600x600")
    list = {
        "A4":2,
        "S4":3
    }
    

    header_database = [
        "4x4",
        "4x5",
        "4x6"
    ]

    gui = GUI(root,list,header_database)



    variable = StringVar(root)
    variable.set("Select energetic")
    energetics = OptionMenu(root, variable, *energetic.Energetics(list).get_energetics())
    energetics.place(x=150, y = 50, anchor='nw')

    variable2 = StringVar(root)
    variable2.set("Select header size")
    headers = OptionMenu(root, variable2, *header_database)
    headers.place(x=450,y=50,anchor='ne')

    add_energetic_button = Button(root, text = "Add energetic", command = gui.new_window_energetic)
    add_energetic_button.place(x = 250, y=85)

    root.mainloop()