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
        '''
        Creates drop down menus to select certain energetics or header sizes
        '''
        variable = StringVar(self.master)
        variable.set("Select energetic")
        energetics = OptionMenu(self.master, variable, *self.energetic.get_energetics())
        energetics.place(x=150, y = 50, anchor='nw')

        variable2 = StringVar(self.master)
        variable2.set("Select header size")
        headers = OptionMenu(self.master, variable2, *self.header.get_header())
        headers.place(x=450,y=50,anchor='ne')

        

    def button(self):
        '''
        Creates a button add more energetics or header types
        '''
        add_energetic_button = Button(self.master, text = "Add energetic", command = self.new_window_energetic)
        add_energetic_button.place(x = 250, y=85)

    def draw_header(self):
        '''
        Creates a visualisation of the header
        '''
        canvas = Canvas(self.master)
        canvas.create_rectangle(230,10,290,70)
        canvas.create_rectangle(170,10,230,70)
        canvas.create_rectangle(230,70,290,130)
        canvas.create_rectangle(170,70,230,130)
        canvas.place(x=100,y=100)

    def submit(self, master):
        '''
        Submit button that confirms a newly added header or energetic
        '''
        energetic_name = self.name_energetic.get()
        energetic_roi = self.ROI_energetic.get()
        self.energetic.add_energetics([energetic_name,energetic_roi])
        print(self.energetic.get_energetics())
        master.destroy() 
        self.refresh()
    
    def new_window_energetic(self):
        '''
        Creates a new window for user to enter a new energetic or header
        '''
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
        self.master.destroy()
        self.__init__(self.master, self.energetic, self.header)



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
    gui.drop_menu()

    root.mainloop()