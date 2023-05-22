# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Tkinter: address book) Rewrite the address book case study in Section 13.12 with
the following improvements, as shown in Figure 13.14:
(a) Add a new button named Update. Clicking it enables the user to update the
address that is currently displayed.
(b) Add a label below the buttons to display the current address location and the
total number of addresses in the list.
(c) Implement the unfinished processPrevious and processLast methods in
Listing 13.20.'''

import os.path
import pickle
import tkinter.messagebox
from tkinter import *  # Import tkinter


class Address:
    def __init__(self, name, street, city, state, zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


class AddressBook:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("AddressBook")  # Set title

        self.nameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Name").grid(row=1,
                                        column=1, sticky=W)
        Entry(frame1, textvariable=self.nameVar,
              width=40).grid(row=1, column=2)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text="Street").grid(row=1,
                                          column=1, sticky=W)
        Entry(frame2, textvariable=self.streetVar,
              width=40).grid(row=1, column=2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="City", width=5).grid(row=1,
                                                 column=1, sticky=W)
        Entry(frame3,
              textvariable=self.cityVar).grid(row=1, column=2)
        Label(frame3, text="State").grid(row=1,
                                         column=3, sticky=W)
        Entry(frame3, textvariable=self.stateVar,
              width=5).grid(row=1, column=4)
        Label(frame3, text="ZIP").grid(row=1,
                                       column=5, sticky=W)
        Entry(frame3, textvariable=self.zipVar,
              width=5).grid(row=1, column=6)

        frame4 = Frame(window)
        frame4.pack()
        Button(frame4, text="Add",
               command=self.processAdd).grid(row=1, column=1)
        btFirst = Button(frame4, text="First",
                         command=self.processFirst).grid(row=1, column=2)
        btNext = Button(frame4, text="Next",
                        command=self.processNext).grid(row=1, column=3)
        btPrevious = Button(frame4, text="Previous", command=
        self.processPrevious).grid(row=1, column=4)
        btLast = Button(frame4, text="Last",
                        command=self.processLast).grid(row=1, column=5)

        self.addressList = self.loadAddress()
        self.current = 0

        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop()  # Create an event loop

    def saveAddress(self):
        outputFile = open("address.dat", "wb")
        pickle.dump(self.addressList, outputFile)
        tkinter.messagebox.showinfo(
            "Address saved", "A new address is saved")
        outputFile.close()

    def loadAddress(self):
        if not os.path.isfile("address.dat"):
            return []  # Return an empty list

        try:
            inputFile = open("address.dat", "rb")
            addressList = pickle.load(inputFile)
        except EOFError:
            addressList = []

        inputFile.close()
        return addressList

    def processAdd(self):
        address = Address(self.nameVar.get(),
                          self.streetVar.get(), self.cityVar.get(),
                          self.stateVar.get(), self.zipVar.get())
        self.addressList.append(address)
        self.saveAddress()

    def processFirst(self):
        self.current = 0
        self.setAddress()

    def processNext(self):
        if self.current < len(self.addressList) - 1:
            self.current += 1
            self.setAddress()

    def processPrevious(self):
        pass  # To Be Continue

    def processLast(self):
        pass  # To Be Continue

    def setAddress(self):
        self.nameVar.set(self.addressList[self.current].name)
        self.streetVar.set(self.addressList[self.current].street)
        self.cityVar.set(self.addressList[self.current].city)
        self.stateVar.set(self.addressList[self.current].state)
        self.zipVar.set(self.addressList[self.current].zip)


AddressBook()  # Create GUI
