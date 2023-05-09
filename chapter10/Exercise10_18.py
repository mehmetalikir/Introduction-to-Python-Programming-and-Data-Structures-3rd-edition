# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Student Registration) Write a program that creates a user interface for student
registrations, as shown in Figure 10.24a'''

from tkinter import *  # Import tkinter


class StudentRegistration:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Student Registration")  # Set title

        self.firstnameVar = StringVar()
        self.midinitialsVar = StringVar()
        self.studentidVar = StringVar()
        self.programVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="First Name").grid(row=1, column=1, sticky=W)
        Entry(frame1, textvariable=self.firstnameVar).grid(row=1, column=2)
        Label(frame1, text="Middle Initials").grid(row=1, column=3, sticky=W)
        Entry(frame1, textvariable=self.midinitialsVar, width=5).grid(row=1, column=4)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text="Student ID").grid(row=2,
                                              column=1, sticky=W)
        Entry(frame2, textvariable=self.studentidVar,
              width=37).grid(row=2, column=2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="Program").grid(row=5, column=1, sticky=W)
        Entry(frame3, textvariable=self.programVar,
              width=37).grid(row=5, column=2)

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

        window.mainloop()  # Create an event loop

    def processAdd(self):
        pass

    def processFirst(self):
        pass

    def processNext(self):
        pass

    def processPrevious(self):
        pass

    def processLast(self):
        pass


StudentRegistration()  # Create GUI
