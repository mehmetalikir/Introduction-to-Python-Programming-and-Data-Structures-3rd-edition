# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Display selected sized shape) Write a program that contains a combo box and
a canvas. The combo box show three strings: Small, Medium and Large. The canvas
displays a shape with size according to the selection in the combo box, as shown in
Figure 11.13'''

from tkinter import *  # Import tkinter


class DisplayShape:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Select Shapes")  # Set title

        # Create a combo box to select shape
        var = StringVar()
        var.set("rectangle")  # initial value
        comboBox = OptionMenu(window, var, "rectangle", "oval", "arc",
                              command=self.processSelection).pack(fill=BOTH)

        # Place self.canvas in the window
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        window.mainloop()  # Create an event loop

    # Display text as per selected font
    def processSelection(self, selectedItem):
        self.canvas.delete("shapes")
        if selectedItem == "rectangle":
            self.canvas.create_rectangle(10, 10, 190, 90, fill="", tags="shapes")
        elif selectedItem == "oval":
            self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="shapes")
        else:
            self.canvas.create_arc(10, 10, 190, 90, fill="red", tags="shapes")


DisplayShape()  # Create GUI
