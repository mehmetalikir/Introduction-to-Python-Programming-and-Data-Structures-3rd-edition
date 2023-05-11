# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Change font type) Write a program that contains a combo box and a label. The
combo box shows five strings: Arial, Verdana, Helvetica, Times, and Courier.
The label displays the string: "Programing is fun" with the specified font type
from the combo box, as shown in Figure 11.14'''
from tkinter import *  # Import tkinter


class ChangeFontType:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Set Font Type")  # Set title

        # Create a combo box to select font
        var = StringVar()
        var.set("Arial")  # initial value
        comboBox = OptionMenu(window, var, "Arial", "Times", "Courier",
                              command=self.processSelection).pack(fill=BOTH)

        self.label = Label(window, text="Programming is fun", font="Arial")
        self.label["font"] = "Arial"
        self.label.pack()

        window.mainloop()  # Create an event loop

    # Display text as per selected font
    def processSelection(self, selectedItem):
        self.label["font"] = selectedItem


ChangeFontType()  # Create GUI
