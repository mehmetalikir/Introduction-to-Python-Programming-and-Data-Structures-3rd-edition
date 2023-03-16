# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Financial application: payroll) Write a program that reads the following information
and prints a payroll statement:
'''

# Prompt the user for input
name = str(input("Employee’s name: "))
hoursPerWeek = float(input("Number of hours worked in a week: "))
payRate = float(input("Hourly pay rate: "))
federalTax = float(input("Federal tax withholding rate: "))
stateTax = float(input("State tax withholding rate: "))

print("")

# Print payroll statement
grossPay = hoursPerWeek * payRate
federal = grossPay * federalTax
state = grossPay * stateTax
totalDeduction = federal + state
print(f"Employee Name: ", name,
      "\nHours Worked: ", hoursPerWeek,
      "\nPay Rate: $", payRate,
      "\nGross Pay: $", format(grossPay, ".2f"),
      "\nDeductions:"
      "\n  Federal Withholding (20.0%): $", format(federal, ".2f"),
      "\n  State Withholding (9.0%): $", round(state, 2),
      "\n  Total Deduction: $", format(totalDeduction, ".2f"),
      "\n",
      "\nNet Pay: $", format((grossPay - totalDeduction), ".2f"))
