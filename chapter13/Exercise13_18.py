# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Process large dataset) A university posts its employee salary at
https://liveexample.pearsoncmg.com/data/Salary.txt. Each line in the file consists
of faculty first name, last name, rank, and salary (see Exercise 13.16).
Write a program to display the total salary for assistant professors,
associate professors, full professors, and all faculty, respectively,
and display the average salary for assistant professors,
associate professors, full professors, and all faculty, respectively.'''

import urllib.request

inputFile = urllib.request.urlopen("https://liveexample.pearsoncmg.com/data/Salary.txt")

totalAssistant = totalAssociate = totalFull = total = 0
countAssistant = countAssociate = countFull = 0
for line in inputFile:
    items = line.split()
    total += float(items[3])

    if items[2].decode() == "assistant":
        totalAssistant += float(items[3])
        countAssistant += 1
    elif items[2].decode() == "associate":
        totalAssociate += float(items[3])
        countAssociate += 1
    else:
        if items[2].decode() == "full":
            totalFull += float(items[3])
            countFull += 1

print("Total salary for assistant professors: ", format(totalAssistant, ".2f"))
print("Total salary for associate professors: ", format(totalAssociate, ".2f"))
print("Total salary for full professors: ", format(totalFull, ".2f"))
print("Average salary for assistant professors: ", format(totalAssistant / countAssistant, ".2f"))
print("Average salary for associate professors: ", format(totalAssociate / countAssociate, ".2f"))
print("Average salary for full professors: ", format(totalFull / countFull, ".2f"))