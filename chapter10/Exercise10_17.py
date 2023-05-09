# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Compare loans with various interest rates) Rewrite Exercise 5.23 to create the
user interface shown in Figure 10.23b. Your program should let the user enter the
loan amount and loan period in the number of years from a text field, and should
display the monthly and total payments for each interest rate starting from 5 percent
to 8 percent, with increments of one-eighth, in a text area.'''

from tkinter import *  # Import tkinter


class MainGUI:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Compare Interest Rates")

        frame = Frame(window)
        frame.pack()

        # Assign values
        self.loanAmount = StringVar()
        self.years = StringVar()

        Label(frame, text="Loan Amount").grid(row=1, column=1, sticky=W)
        Entry(frame, textvariable=self.loanAmount).grid(row=1, column=2)
        Label(frame, text="Years").grid(row=1, column=3, sticky=W)
        Entry(frame, textvariable=self.years).grid(row=1, column=4)
        Button(frame, text="Calculate", command=self.calculateLoan).grid(row=1, column=5, sticky=E)

        self.canvas = Canvas(window, width=400, height=400, bg="white")
        self.canvas.pack()

        window.mainloop()  # Create an event loop

    def calculateLoan(self):
        import math

        # Constant
        ANNUAL_INTEREST_RATE = 5.0

        # Prompt the user enter the loan amount and loan period in numbers of years
        loanAmount = float(self.loanAmount.get())
        years = float(self.years.get())

        # Format header
        s = ("%-1s%20s%20s" % ("Interest Rate", "Monthly Payment", "Total Payment"))
        self.canvas.create_text(145, 10, text=s, justify=LEFT, font="Times 10 bold underline")

        i = 5
        # Display result
        while ANNUAL_INTEREST_RATE <= 8:
            monthlyInterestRate = ANNUAL_INTEREST_RATE / 1200
            monthlyPayment = loanAmount * monthlyInterestRate / (1
                                                                 - 1 / math.pow(1 + monthlyInterestRate, years * 12))
            s1 = (f"%-1.3f%s%20.2f%22.2f" % (ANNUAL_INTEREST_RATE, "%", monthlyPayment, (monthlyPayment * 12) * years))
            ANNUAL_INTEREST_RATE += 1 / 8

            self.canvas.create_text(135, 5 * i, text=s1, justify=LEFT)
            i += 2


MainGUI()  # Create GUI
