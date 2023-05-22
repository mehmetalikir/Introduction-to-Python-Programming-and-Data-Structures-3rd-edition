# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Create large dataset) Create a data file with 1000 lines. Each line in the file
consists of a person's title(Mr or Mrs), their last name and a score they achieved.
Last names should be randomly selected from a set of 5 names(Brown, Smith,
Wolf, Morse, Rogers). The gender is randomly generated and must be a value
between 0 and 100. The data should be saved in a file called Scores.txt. Here is
some possible sample data:'''

import random


def main():
    outputFile = open("Scores.txt", "w")

    names = ["Brown", "Smith", "Wolf", "Morse", "Rogers"]

    N = 1000
    for i in range(N):
        gender = random.randint(0, 1)
        if gender == 0:
            outputFile.write("Mrs " + names[random.randint(0, len(names) - 1)] + " - ")
        else:
            outputFile.write("Mr " + names[random.randint(0, len(names) - 1)] + " - ")

        outputFile.write("Score: ")
        outputFile.write(str(random.randint(0, 100)) + "%")

        if i < N - 1:
            outputFile.write("\n")

    outputFile.close()


main()
